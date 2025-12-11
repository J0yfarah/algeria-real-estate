import pandas as pd
from pandas import json_normalize

def flatten_announcement(raw_json: dict) -> dict:
    """
    Takes the nested announcement JSON returned by GraphQL
    and returns a flattened dictionary suitable for DataFrame/Parquet.
    """
    if raw_json is None:
        return {}
    try:
        flat = json_normalize(
            raw_json,
            sep="_",
            max_level=3
        ).to_dict(orient="records")[0]
        return flat
    except Exception:
        return raw_json
