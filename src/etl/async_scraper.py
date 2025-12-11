import asyncio
import aiohttp
import pandas as pd
import json
import time
from pathlib import Path
from tqdm.asyncio import tqdm
from flattener import flatten_announcement


# ---------------------------------------------------
# Configuration
# ---------------------------------------------------
INPUT_CSV = Path(__file__).resolve().parents[2] / "data" / "raw" / "immobilier.csv"

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "data" / "raw" / "api_details"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)  # create if doesn't exist


LOG_FILE = Path("logs/scraper.log")
LOG_FILE.parent.mkdir(exist_ok=True, parents=True)

BATCH_SIZE = 1000
CONCURRENCY = 25               # parallel requests
MAX_RETRIES = 5
GRAPHQL_URL = "https://www.ouedkniss.com/graphql"

# Optional proxy rotation (leave empty for no proxy)
PROXIES = [
]


QUERY = """
query AnnouncementGet($id: ID!) {
  announcement: announcementDetails(id: $id) {
    id
    reference
    title
    slug
    description
    createdAt: refreshedAt
    price
    priceType
    priceUnit
    street_name
    category { id name slug }
    specs {
      specification { label codename type }
      value
      valueText
    }
    cities {
      id
      name
      region { id name slug }
    }
    medias { mediaUrl mimeType }
    user { id username displayName }
  }
}
"""

# ---------------------------------------------------
# Logging helper
# ---------------------------------------------------
def log(msg: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}  {msg}\n")
    print(msg)

# ---------------------------------------------------
# Proxy rotator
# ---------------------------------------------------
def get_proxy(i: int):
    if not PROXIES:
        return None
    return PROXIES[i % len(PROXIES)]

# ---------------------------------------------------
# Async fetch with retry & backoff
# ---------------------------------------------------
async def fetch_one(session, id_value: str, index: int):
    payload = {"query": QUERY, "variables": {"id": id_value}}
    proxy = get_proxy(index)

    for attempt in range(MAX_RETRIES):
        try:
            async with session.post(
                GRAPHQL_URL,
                json=payload,
                proxy=proxy,
                timeout=aiohttp.ClientTimeout(total=12)
            ) as resp:

                if resp.status != 200:
                    await asyncio.sleep(0.5 * (attempt + 1))
                    continue

                data = await resp.json()

                if "errors" in data:
                    return {"id": id_value, "error": data["errors"]}

                return data.get("data", {}).get("announcement", None)

        except Exception as e:
            await asyncio.sleep(0.5 * (attempt + 1))

    return {"id": id_value, "error": f"Failed after {MAX_RETRIES} retries"}

# ---------------------------------------------------
# Process one batch (async)
# ---------------------------------------------------
async def process_batch(batch_ids, batch_num):
    connector = aiohttp.TCPConnector(limit=CONCURRENCY)
    async with aiohttp.ClientSession(connector=connector) as session:

        results = []

        for i in tqdm(range(len(batch_ids)), desc=f"Batch {batch_num}", ncols=90):
            id_val = batch_ids[i]
            res = await fetch_one(session, id_val, i)
            flat = flatten_announcement(res)
            flat["original_id"] = id_val
            results.append(flat)

        df = pd.DataFrame(results)

        output_path = OUTPUT_DIR / f"batch_{batch_num}.parquet"
        df.to_parquet(output_path, index=False)

        log(f"Saved batch {batch_num} → {output_path}")


# ---------------------------------------------------
# Auto-resume logic
# ---------------------------------------------------
def get_last_completed_batch():
    files = list(OUTPUT_DIR.glob("batch_*.parquet"))
    if not files:
        return 0
    nums = [int(f.stem.split("_")[1]) for f in files]
    return max(nums)


# ---------------------------------------------------
# Main runner
# ---------------------------------------------------
async def main():
    df = pd.read_csv(INPUT_CSV)

    if "id" not in df.columns:
        raise Exception("CSV must contain column 'id'")

    ids = df["id"].astype(str).tolist()
    total = len(ids)

    log(f"Loaded {total} IDs.")

    start_batch = get_last_completed_batch() + 1

    log(f"Auto-resume enabled. Starting from batch {start_batch}.")

    for offset in range((start_batch-1) * BATCH_SIZE, total, BATCH_SIZE):
        batch_num = offset // BATCH_SIZE + 1
        batch_ids = ids[offset : offset + BATCH_SIZE]

        log(f"Starting batch {batch_num} ({len(batch_ids)} IDs)")

        await process_batch(batch_ids, batch_num)

    log("All batches completed successfully.")


if __name__ == "__main__":
    asyncio.run(main())
