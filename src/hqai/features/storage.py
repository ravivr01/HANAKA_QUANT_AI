"""
==========================================================
HQAI Feature Storage
==========================================================

Stores calculated features as Parquet files.

Author  : Ravi Varma
Version : 0.8.1
==========================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from hqai.core.logger import log
from hqai.features.config import feature_config


class FeatureStorage:
    """
    Handles reading and writing of feature files.
    """

    def __init__(self):

        self.feature_dir = feature_config.FEATURE_DIR

    # --------------------------------------------------
    # Get Feature File
    # --------------------------------------------------

    def feature_file(
        self,
        symbol: str,
    ) -> Path:

        return self.feature_dir / f"{symbol}.parquet"

    # --------------------------------------------------
    # Exists
    # --------------------------------------------------

    def exists(
        self,
        symbol: str,
    ) -> bool:

        return self.feature_file(symbol).exists()

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    def save(
        self,
        symbol: str,
        dataframe: pd.DataFrame,
    ) -> Path:

        file = self.feature_file(symbol)

        dataframe.to_parquet(
            file,
            index=False,
            compression=feature_config.COMPRESSION,
        )

        log.info(f"Saved -> {file.name}")

        return file

    # --------------------------------------------------
    # Load
    # --------------------------------------------------

    def load(
        self,
        symbol: str,
    ) -> pd.DataFrame:

        file = self.feature_file(symbol)

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

        file = self.feature_file(symbol)

        if file.exists():

            file.unlink()

            log.info(f"Deleted -> {file.name}")

    # --------------------------------------------------
    # List Files
    # --------------------------------------------------

    def list_symbols(self):

        return sorted(

            file.stem

            for file in self.feature_dir.glob("*.parquet")

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

            f.stat().st_size

            for f in self.feature_dir.glob("*.parquet")

        )

        return total / (1024 * 1024)

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self):

        print()
        print("=" * 60)
        print("HQAI FEATURE STORAGE")
        print("=" * 60)
        print(f"Directory : {self.feature_dir}")
        print(f"Files     : {self.count()}")
        print(f"Disk (MB) : {self.disk_usage():.2f}")
        print("=" * 60)