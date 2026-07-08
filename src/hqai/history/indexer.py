"""
==========================================================
HQAI History Index Rebuilder
==========================================================

Scans existing Parquet history files and rebuilds the
history_index table.

Author  : Ravi Varma
Version : 1.0
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import polars as pl

from hqai.core.database import db
from hqai.core.logger import log


class HistoryIndexer:

    def __init__(self):

        self.history_folder = Path("data/bronze/history")

    ########################################################

    def rebuild(self):

        log.info("=" * 60)
        log.info("Rebuilding History Index")
        log.info("=" * 60)

        db.execute("DELETE FROM history_index")

        total = 0

        for file in sorted(self.history_folder.glob("*/history.parquet")):

            symbol = file.parent.name

            try:

                df = pl.read_parquet(file)

                rows = df.height

                first_date = df["Date"].min()

                last_date = df["Date"].max()

                sql = f"""
                INSERT INTO history_index
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

                total += 1

                if total % 100 == 0:

                    log.info(f"Indexed {total} symbols")

            except Exception as ex:

                log.error(f"{symbol} -> {ex}")

        log.success("=" * 60)
        log.success(f"Indexed {total} symbols")
        log.success("=" * 60)
