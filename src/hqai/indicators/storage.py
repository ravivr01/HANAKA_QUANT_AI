"""
==========================================================
HQAI Indicator Storage
==========================================================

Stores indicator datasets in the Silver Layer.

Author  : Ravi Varma
Release : 0.9.1
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import polars as pl

from hqai.core.database import db
from hqai.core.logger import log


class IndicatorStorage:
    """
    Silver Layer Storage for Indicators.
    """

    def __init__(self):

        self.output = Path("data/silver/indicators")

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

        return folder / "indicators.parquet"

    ########################################################

    def save(
        self,
        df: pd.DataFrame,
        symbol: str,
    ):

        file = self.symbol_path(symbol)

        pl.from_pandas(df).write_parquet(file)

        log.success(f"Saved {file}")

        return file

    ########################################################

    def load(
        self,
        symbol: str,
    ) -> pl.DataFrame:

        return pl.read_parquet(self.symbol_path(symbol))

    ########################################################

    def exists(
        self,
        symbol: str,
    ) -> bool:

        return self.symbol_path(symbol).exists()

    ########################################################

    def register(
        self,
        symbol: str,
    ):

        db.register_parquet(
            f"indicators_{symbol.lower()}",
            str(self.symbol_path(symbol)),
        )

        log.info(f"Registered indicators_{symbol.lower()}")

    ########################################################

    def delete(
        self,
        symbol: str,
    ):

        file = self.symbol_path(symbol)

        if file.exists():

            file.unlink()

            log.warning(f"Deleted {file}")
