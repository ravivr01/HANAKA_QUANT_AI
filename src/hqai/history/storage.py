"""
==========================================================
HQAI History Storage
==========================================================

Responsible for persisting historical market data.

Author  : Ravi Varma
Version : 1.0
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import polars as pl

from hqai.core.database import db
from hqai.core.logger import log


class HistoryStorage:

    def __init__(self):

        self.output = Path("data/bronze/history")

        self.output.mkdir(
            parents=True,
            exist_ok=True,
        )

    # --------------------------------------------------

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

    # --------------------------------------------------

    def save(
        self,
        df: pd.DataFrame,
        symbol: str,
    ):

        file = self.symbol_path(symbol)

        pl.from_pandas(df).write_parquet(file)

        log.success(f"Saved {file}")

        return file

    # --------------------------------------------------

    def load(
        self,
        symbol: str,
    ) -> pl.DataFrame:

        file = self.symbol_path(symbol)

        return pl.read_parquet(file)

    # --------------------------------------------------

    def exists(
        self,
        symbol: str,
    ) -> bool:

        return self.symbol_path(symbol).exists()

    # --------------------------------------------------

    def register(
        self,
        symbol: str,
    ):

        file = self.symbol_path(symbol)

        db.register_parquet(
            symbol,
            str(file),
        )

        log.info(
            f"Registered {symbol}"
        )

    # --------------------------------------------------

    def delete(
        self,
        symbol: str,
    ):

        file = self.symbol_path(symbol)

        if file.exists():

            file.unlink()

            log.warning(
                f"Deleted {symbol}"
            )