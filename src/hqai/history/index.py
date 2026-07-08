"""
==========================================================
HQAI History Index
==========================================================

Maintains the download status of historical data.

Author : Ravi Varma
Version : 1.0
"""

from __future__ import annotations

from datetime import datetime

import pandas as pd

from hqai.core.database import db
from hqai.core.logger import log


class HistoryIndex:

    def update(
        self,
        symbol: str,
        df: pd.DataFrame,
        status: str = "SUCCESS",
    ):

        rows = len(df)

        first_date = df["Date"].min()

        last_date = df["Date"].max()

        sql = f"""
        INSERT OR REPLACE INTO history_index
        VALUES
        (
            '{symbol}',
            {rows},
            DATE '{first_date:%Y-%m-%d}',
            DATE '{last_date:%Y-%m-%d}',
            TIMESTAMP '{datetime.now():%Y-%m-%d %H:%M:%S}',
            '{status}'
        )
        """

        db.execute(sql)

        log.success(f"Indexed {symbol}")

    ####################################################

    def failed(
        self,
        symbol: str,
        reason: str = "",
    ):

        sql = f"""
        INSERT OR REPLACE INTO history_index
        VALUES
        (
            '{symbol}',
            0,
            NULL,
            NULL,
            TIMESTAMP '{datetime.now():%Y-%m-%d %H:%M:%S}',
            'FAILED'
        )
        """

        db.execute(sql)

        log.warning(f"{symbol} marked FAILED")