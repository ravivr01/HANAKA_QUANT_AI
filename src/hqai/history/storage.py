"""
==========================================================
HQAI History Storage
Release : 0.6
Author  : Hanaka Quant AI

Responsible for persisting historical market data.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
import polars as pl

from hqai.core.database import db
from hqai.core.logger import log


class HistoryStorage:
    """
    Storage Manager for Historical Data.

    Responsibilities
    ----------------
    - Save Parquet
    - Load Parquet
    - Register DuckDB View
    - Maintain history_index
    - Delete Symbol History
    """

    def __init__(self):

        self.output = Path("data/bronze/history")

        self.output.mkdir(
            parents=True,
            exist_ok=True,
        )

    ########################################################

    def symbol_path(
        self,
        symbol: str,
    ) -> Path:

        folder = self.output / symbol

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        return folder / "history.parquet"

    ########################################################

    def exists(
        self,
        symbol: str,
    ) -> bool:

        return self.symbol_path(symbol).exists()

    ########################################################

    def save(
        self,
        df: pd.DataFrame,
        symbol: str,
    ) -> Path:

        file = self.symbol_path(symbol)

        # Convert Pandas -> Polars
        pl_df = pl.from_pandas(df)

        # Save
        pl_df.write_parquet(file)

        # Register in DuckDB
        self.register(symbol)

        # Update index
        self.update_index(symbol, df)

        log.success(f"{symbol} saved.")

        return file

    ########################################################

    def load(
        self,
        symbol: str,
    ) -> pl.DataFrame:

        return pl.read_parquet(self.symbol_path(symbol))

    ########################################################

    def register(
        self,
        symbol: str,
    ):

        file = self.symbol_path(symbol)

        db.register_parquet(
            f"history_{symbol.lower()}",
            str(file),
        )

    ########################################################

    def update_index(
        self,
        symbol: str,
        df: pd.DataFrame,
    ):

        rows = len(df)

        first_date = pd.to_datetime(df["Date"]).min()

        last_date = pd.to_datetime(df["Date"]).max()

        sql = f"""
        INSERT OR REPLACE INTO history_index
        VALUES
        (
            '{symbol}',
            {rows},
            DATE '{first_date:%Y-%m-%d}',
            DATE '{last_date:%Y-%m-%d}',
            TIMESTAMP '{datetime.now():%Y-%m-%d %H:%M:%S}',
            'SUCCESS'
        )
        """

        db.execute(sql)

    ########################################################

    def mark_failed(
        self,
        symbol: str,
        reason: str = "",
    ):

        sql = f"""
        INSERT OR REPLACE INTO history_index
        VALUES
        (
            '{symbol}',
            0,
            NULL,
            NULL,
            TIMESTAMP '{datetime.now():%Y-%m-%d %H:%M:%S}',
            'FAILED'
        )
        """

        db.execute(sql)

        log.warning(f"{symbol} marked FAILED")

    ########################################################

    def delete(
        self,
        symbol: str,
    ):

        file = self.symbol_path(symbol)

        if file.exists():

            file.unlink()

            log.warning(f"{symbol} deleted.")

        db.execute(f"DELETE FROM history_index WHERE symbol='{symbol}'")

    ########################################################

    def summary(self):

        return db.query("""
            SELECT
                status,
                COUNT(*) AS symbols
            FROM history_index
            GROUP BY status
            ORDER BY status
            """)
