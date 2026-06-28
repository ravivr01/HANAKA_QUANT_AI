"""
============================================================
HQAI Universe Metadata
============================================================
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import pandas as pd

from hqai.core.config import config
from hqai.core.logger import log


class UniverseMetadata:

    def __init__(self):

        self.output_dir = (
            config.data_dir /
            "bronze" /
            "universe"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.metadata_file = (
            self.output_dir /
            "metadata.json"
        )

    ########################################################

    def generate(self, dataframe: pd.DataFrame):

        metadata = {
            "generated_at": datetime.utcnow().isoformat(),
            "records": int(len(dataframe)),
            "columns": int(len(dataframe.columns)),
            "column_names": dataframe.columns.tolist(),
            "source": "NSE",
            "csv_file": "universe.csv",
            "parquet_file": "universe.parquet",
            "duckdb_table": "universe",
            "hqai_version": "0.3.0",
        }

        with open(
            self.metadata_file,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
            )

        log.info(
            f"Metadata Saved -> {self.metadata_file}"
        )
