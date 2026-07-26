"""
HQAI Feature Metadata
"""

from datetime import datetime
import json


class FeatureMetadata:

    def generate(
        self,
        symbol,
        rows,
        first_date,
        last_date,
    ):

        return {

            "symbol": symbol,

            "rows": rows,

            "first_date": str(first_date),

            "last_date": str(last_date),

            "generated_at": str(datetime.now()),

            "version": "0.8.0",

        }

    def save(
        self,
        metadata,
        file,
    ):

        with open(file, "w") as f:

            json.dump(
                metadata,
                f,
                indent=4,
            )