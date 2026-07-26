"""
==========================================================
HQAI History Updater
==========================================================

Updates existing history by downloading only missing data.

Author  : Ravi Varma
Version : 0.7.4
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yfinance as yf
from loguru import logger

from hqai.core.config import config


class HistoryUpdater:

    def __init__(self):

        self.history_dir = config.data_dir / "bronze" / "history"

    # -----------------------------------------------------

    def history_files(self):

        return sorted(self.history_dir.rglob("*.parquet"))

    # -----------------------------------------------------

    def symbol_from_file(self, file: Path):

        if file.name == "history.parquet":
            return file.parent.name

        return file.stem

    # -----------------------------------------------------

    def latest_date(self, df):

        return pd.to_datetime(df["Date"]).max()

    # -----------------------------------------------------

    def update_symbol(self, file: Path):

        symbol = self.symbol_from_file(file)

        logger.info(f"Updating {symbol}")

        try:

            df_old = pd.read_parquet(file)

            last_date = self.latest_date(df_old)

            df_new = yf.download(
                f"{symbol}.NS",
                start=last_date.strftime("%Y-%m-%d"),
                interval="1d",
                progress=False,
                auto_adjust=False,
                threads=False,
            )

            if df_new.empty:

                logger.info(f"{symbol} already up-to-date")

                return "SKIPPED"

            df_new.reset_index(inplace=True)

            if isinstance(df_new.columns, pd.MultiIndex):
                df_new.columns = [c[0] for c in df_new.columns]

            df_all = pd.concat(
                [df_old, df_new],
                ignore_index=True,
            )

            df_all.drop_duplicates(
                subset=["Date"],
                inplace=True,
            )

            df_all.to_parquet(
                file,
                index=False,
            )

            logger.success(f"{symbol} updated")

            return "UPDATED"

        except Exception as ex:

            logger.error(f"{symbol} -> {ex}")

            return "FAILED"

    # -----------------------------------------------------

    def run(self):

        files = self.history_files()

        updated = 0
        skipped = 0
        failed = 0

        print()
        print("=" * 70)
        print("HQAI HISTORY UPDATE")
        print("=" * 70)
        print()

        print(f"Symbols : {len(files)}")
        print()

        for file in files:

            status = self.update_symbol(file)

            if status == "UPDATED":
                updated += 1

            elif status == "SKIPPED":
                skipped += 1

            else:
                failed += 1

        print()
        print("=" * 70)
        print("SUMMARY")
        print("=" * 70)
        print(f"Updated : {updated}")
        print(f"Skipped : {skipped}")
        print(f"Failed  : {failed}")
        print("=" * 70)