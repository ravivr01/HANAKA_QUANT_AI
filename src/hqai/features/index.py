"""
==========================================================
HQAI Feature Index
==========================================================

Maintains the Feature Index inside DuckDB.

Author  : Ravi Varma
Version : 0.8.3
==========================================================
"""

from datetime import datetime

from hqai.core.database import db
from hqai.core.logger import log


class FeatureIndex:

    def __init__(self):

        self.create()

    # --------------------------------------------------
    # Create Table
    # --------------------------------------------------

    def create(self):

        db.execute(
            """
            CREATE TABLE IF NOT EXISTS feature_index(

                SYMBOL VARCHAR PRIMARY KEY,

                ROWS BIGINT,

                FIRST_DATE DATE,

                LAST_DATE DATE,

                UPDATED_AT TIMESTAMP,

                VERSION VARCHAR,

                STATUS VARCHAR

            )
            """
        )

    # --------------------------------------------------
    # Upsert
    # --------------------------------------------------

    def update(
        self,
        symbol,
        rows,
        first_date,
        last_date,
        version="0.8.3",
        status="SUCCESS",
    ):

        db.execute(
            f"""
            DELETE FROM feature_index
            WHERE SYMBOL='{symbol}'
            """
        )

        db.execute(
            f"""
            INSERT INTO feature_index VALUES(

                '{symbol}',

                {rows},

                '{first_date}',

                '{last_date}',

                CURRENT_TIMESTAMP,

                '{version}',

                '{status}'

            )
            """
        )

    # --------------------------------------------------
    # Count
    # --------------------------------------------------

    def count(self):

        return db.query(
            """
            SELECT COUNT(*) AS COUNT

            FROM feature_index
            """
        )["COUNT"][0]

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def stats(self):

        return db.query(
            """
            SELECT *

            FROM feature_index

            ORDER BY SYMBOL
            """
        )


feature_index = FeatureIndex()