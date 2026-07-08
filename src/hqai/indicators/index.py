"""
==========================================================
HQAI Indicator Index
==========================================================

Maintains metadata for generated indicator datasets.

Author  : Ravi Varma
Release : 0.9.4
"""

from __future__ import annotations


import polars as pl

from hqai.core.database import db
from hqai.core.logger import log


class IndicatorIndex:
    """
    Maintains the indicator_index table.
    """

    ########################################################

    def update(
        self,
        symbol: str,
        df: pl.DataFrame,
        indicators: int,
        version: str = "1.0",
    ):

        sql = f"""
        INSERT OR REPLACE INTO indicator_index
        VALUES (
            '{symbol}',
            {indicators},
            {len(df)},
            DATE '{df["Date"].min()}',
            DATE '{df["Date"].max()}',
            CURRENT_TIMESTAMP,
            '{version}',
            'READY'
        )
        """

        db.execute(sql)

        log.success(f"Indicator Index updated -> {symbol}")

    ########################################################

    def summary(self):

        return db.query("""
            SELECT *
            FROM indicator_index
            ORDER BY symbol
            """)

    ########################################################

    def count(self):

        return db.query("""
            SELECT COUNT(*) AS symbols
            FROM indicator_index
            """)
