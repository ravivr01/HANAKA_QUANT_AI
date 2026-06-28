"""
============================================================
HQAI Universe Storage
============================================================
Stores the NSE Universe into:

1. CSV
2. Parquet
3. DuckDB
============================================================
"""

from pathlib import Path

import duckdb
import pandas as pd

from hqai.core.config import config
from hqai.core.logger import log


class UniverseStorage:
    """
    Handles storage of the NSE universe.
    """

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

        self.csv_file = self.output_dir / "universe.csv"

        self.parquet_file = self.output_dir / "universe.parquet"

        self.duckdb_file = config.duckdb_file

    ########################################################

    def save(self, dataframe: pd.DataFrame):

        self.save_csv(dataframe)

        self.save_parquet(dataframe)

        self.save_duckdb(dataframe)

    ########################################################

    def save_csv(self, dataframe: pd.DataFrame):

        dataframe.to_csv(
            self.csv_file,
            index=False
        )

        log.info(
            f"CSV Saved -> {self.csv_file}"
        )

    ########################################################

    def save_parquet(self, dataframe: pd.DataFrame):

        dataframe.to_parquet(
            self.parquet_file,
            index=False
        )

        log.info(
            f"Parquet Saved -> {self.parquet_file}"
        )

    ########################################################

    def save_duckdb(self, dataframe: pd.DataFrame):

        connection = duckdb.connect(
            str(self.duckdb_file)
        )

        connection.register(
            "universe_df",
            dataframe
        )

        connection.execute(
            """
            CREATE OR REPLACE TABLE universe AS
            SELECT *
            FROM universe_df
            """
        )

        connection.close()

        log.info(
            f"DuckDB Updated -> {self.duckdb_file}"
        )
