"""
==========================================================
HQAI History Repository
Release : R-005-002
Author  : Hanaka Quant AI

Repository for history_index operations.
"""

from __future__ import annotations

import polars as pl

from hqai.core.database import db


class HistoryRepository:
    """
    Repository for history_index table.
    """

    def exists(
        self,
        symbol: str,
    ) -> bool:

        sql = f"""
        SELECT COUNT(*)
        FROM history_index
        WHERE symbol = '{symbol}'
        """

        return db.execute(sql).fetchone()[0] > 0

    ########################################################

    def last_date(
        self,
        symbol: str,
    ):

        sql = f"""
        SELECT last_date
        FROM history_index
        WHERE symbol = '{symbol}'
        """

        result = db.execute(sql).fetchone()

        if result:

            return result[0]

        return None

    ########################################################

    def save(
        self,
        symbol: str,
        rows: int,
        first_date,
        last_date,
        status: str = "SUCCESS",
    ):

        db.execute(
            f"""
            INSERT OR REPLACE INTO history_index
            VALUES (
                '{symbol}',
                {rows},
                '{first_date}',
                '{last_date}',
                CURRENT_TIMESTAMP,
                '{status}'
            )
            """
        )

    ########################################################

    def mark_failed(
        self,
        symbol: str,
        message: str,
    ):

        db.execute(
            f"""
            INSERT OR REPLACE INTO history_index
            VALUES (
                '{symbol}',
                0,
                NULL,
                NULL,
                CURRENT_TIMESTAMP,
                'FAILED'
            )
            """
        )

    ########################################################

    def delete(
        self,
        symbol: str,
    ):

        db.execute(
            f"""
            DELETE
            FROM history_index
            WHERE symbol = '{symbol}'
            """
        )

    ########################################################

    def all(self) -> pl.DataFrame:

        return db.query(
            """
            SELECT *
            FROM history_index
            ORDER BY symbol
            """
        )

    ########################################################

    def missing(
        self,
        universe: pl.DataFrame,
    ) -> pl.DataFrame:

        existing = self.all()

        if existing.is_empty():

            return universe

        return universe.join(
            existing.select("symbol"),
            on="symbol",
            how="anti",
        )

    ########################################################

    def summary(self):

        return db.query(
            """
            SELECT
                status,
                COUNT(*) AS symbols
            FROM history_index
            GROUP BY status
            ORDER BY status
            """
        )


history_repository = HistoryRepository()