import requests
import pandas as pd
import time

URL = "https://api.ouedkniss.com/graphql"

HEADERS = {
    "accept": "*/*",
    "accept-language": "fr",
    "content-type": "application/json",
    "locale": "fr",
    "origin": "https://www.ouedkniss.com",
    "referer": "https://www.ouedkniss.com/immobilier/1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "x-app-version": "3.3.70",
    "x-track-id": "abcd1234",
    "x-track-timestamp": str(int(time.time()))
}

QUERY = (
    "query SearchQuery($q: String, $filter: SearchFilterInput) {"
    " search(q: $q, filter: $filter) {"
    "  announcements {"
    "   data {"
    "    id title slug refreshedAt price priceUnit "
    "    cities { name } "
    "    store { name } "
    "    smallDescription { specification { codename } valueText } "
    "   }"
    "   paginatorInfo { hasMorePages lastPage } "
    "  }"
    " }"
    "}"
)

def extract_area(desc):
    """Safely extracts area (superficie) from smallDescription."""
    if not desc or not isinstance(desc, list):
        return None

    for item in desc:
        if not item or not isinstance(item, dict):
            continue

        spec = item.get("specification")
        if not spec or not isinstance(spec, dict):
            continue

        codename = spec.get("codename", "")
        if "superficie" in str(codename).lower():
            return item.get("valueText")

    return None


def fetch_immobilier():
    all_rows = []
    page = 1

    while True:
        print(f"Fetching page {page}...")

        variables = {
            "q": None,
            "filter": {
                "categorySlug": "immobilier",
                "page": page,
                "orderByField": {"field": "REFRESHED_AT"},
                "count": 48
            }
        }

        payload = {"query": QUERY, "variables": variables}
        response = requests.post(URL, json=payload, headers=HEADERS)

        if response.status_code != 200:
            print("Server error:", response.text)
            break

        data = response.json()["data"]["search"]["announcements"]
        rows = data["data"]

        if not rows:
            break

        for a in rows:
            all_rows.append({
                "id": a.get("id"),
                "title": a.get("title"),
                "slug": a.get("slug"),
                "createdAt": a.get("refreshedAt"),
                "price": a.get("price"),
                "priceUnit": a.get("priceUnit"),
                "area": extract_area(a.get("smallDescription")),
                "city": ", ".join([c.get("name") for c in a.get("cities", [])]),
                "store": (a.get("store") or {}).get("name")
            })

        if not data["paginatorInfo"]["hasMorePages"]:
            break

        page += 1
        time.sleep(1)

    return all_rows


def save_to_csv(data, filename="immobilier.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"Saved {len(df)} rows → {filename}")


if __name__ == "__main__":
    data = fetch_immobilier()
    save_to_csv(data)
