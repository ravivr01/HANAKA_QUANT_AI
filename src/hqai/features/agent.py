"""
==========================================================
HQAI Feature Agent
==========================================================

Build Features for all NSE Symbols.

Author  : Ravi Varma
Version : 0.8.1
==========================================================
"""

from __future__ import annotations

import time
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from hqai.core.logger import log
from hqai.features.builder import FeatureBuilder
from hqai.features.storage import FeatureStorage
from hqai.features.config import feature_config
from hqai.features.index import feature_index


class FeatureAgent:

    def __init__(self):

        self.builder = FeatureBuilder()

        self.storage = FeatureStorage()

        self.history_dir = feature_config.HISTORY_DIR

    # --------------------------------------------------
    # History Files
    # --------------------------------------------------

    def history_files(self):

        files = []

        # Flat structure
        files.extend(
            self.history_dir.glob("*.parquet")
        )

        # Nested structure
        files.extend(
            self.history_dir.glob("*/history.parquet")
        )

        return sorted(files)

    # --------------------------------------------------
    # Symbol Name
    # --------------------------------------------------

    def symbol(self, file: Path):

        if file.name == "history.parquet":

            return file.parent.name

        return file.stem

    # --------------------------------------------------
    # Run
    # --------------------------------------------------

    def run(self):

        start = time.time()

        files = self.history_files()

        total = len(files)

        success = 0

        failed = 0

        skipped = 0

        log.info("=" * 60)
        log.info("HQAI FEATURE BUILD")
        log.info("=" * 60)

        for file in tqdm(

            files,

            desc="Feature Build",

        ):

            symbol = self.symbol(file)

            try:

                if self.storage.exists(symbol):

                    skipped += 1

                    continue

                df = pd.read_parquet(file)

                features = self.builder.build(df)

                self.storage.save(

                    symbol,

                    features,

                )

                feature_index.update(

                     symbol=symbol,

                     rows=len(features),

                    first_date=features["Date"].min(),

                    last_date=features["Date"].max(),

        )

                success += 1

            except Exception as ex:

                failed += 1

                log.error(f"{symbol} -> {ex}")

        elapsed = time.time() - start

        print()

        print("=" * 60)

        print("HQAI FEATURE BUILD")

        print("=" * 60)

        print()

        print(f"History Files : {total}")

        print(f"Generated     : {success}")

        print(f"Skipped       : {skipped}")

        print(f"Failed        : {failed}")

        print(f"Elapsed (s)   : {elapsed:.2f}")

        print()

        print("=" * 60)