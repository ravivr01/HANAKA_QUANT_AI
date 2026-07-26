"""
==========================================================
HQAI Indicator Storage
==========================================================

Stores calculated indicators as Parquet files.

Author  : Ravi Varma
Version : 0.9.0
==========================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from hqai.core.logger import log
from hqai.indicators.config import indicator_config


class IndicatorStorage:
    """
    Handles Indicator Repository.
    """

    def __init__(self):

        self.indicator_dir = indicator_config.INDICATOR_DIR

    # --------------------------------------------------
    # File Path
    # --------------------------------------------------

    def indicator_file(
        self,
        symbol: str,
    ) -> Path:

        return self.indicator_dir / f"{symbol}.parquet"

    # --------------------------------------------------
    # Exists
    # --------------------------------------------------

    def exists(
        self,
        symbol: str,
    ) -> bool:

        return self.indicator_file(symbol).exists()

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    def save(
        self,
        symbol: str,
        dataframe: pd.DataFrame,
    ) -> Path:

        file = self.indicator_file(symbol)

        dataframe.to_parquet(
            file,
            compression=indicator_config.COMPRESSION,
            index=False,
        )

        log.info(f"Indicator Saved -> {file.name}")

        return file

    # --------------------------------------------------
    # Load
    # --------------------------------------------------

    def load(
        self,
        symbol: str,
    ) -> pd.DataFrame:

        file = self.indicator_file(symbol)

        if not file.exists():

            raise FileNotFoundError(file)

        return pd.read_parquet(file)

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete(
        self,
        symbol: str,
    ):

        file = self.indicator_file(symbol)

        if file.exists():

            file.unlink()

            log.info(f"Deleted -> {file.name}")

    # --------------------------------------------------
    # Symbols
    # --------------------------------------------------

    def list_symbols(self):

        return sorted(

            file.stem

            for file in self.indicator_dir.glob("*.parquet")

        )

    # --------------------------------------------------
    # Count
    # --------------------------------------------------

    def count(self) -> int:

        return len(self.list_symbols())

    # --------------------------------------------------
    # Disk Usage
    # --------------------------------------------------

    def disk_usage(self) -> float:

        total = sum(

            file.stat().st_size

            for file in self.indicator_dir.glob("*.parquet")

        )

        return total / (1024 * 1024)

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self):

        print()

        print("=" * 70)

        print("HQAI INDICATOR STORAGE")

        print("=" * 70)

        print(f"Directory : {self.indicator_dir}")

        print(f"Files     : {self.count()}")

        print(f"Disk MB   : {self.disk_usage():.2f}")

        print("=" * 70)