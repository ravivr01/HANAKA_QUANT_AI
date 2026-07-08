"""
==========================================================
HQAI History Updater
==========================================================

Incrementally updates historical market data.

Author  : Ravi Varma
Version : 1.0
"""

from __future__ import annotations

from datetime import timedelta

import pandas as pd

from hqai.core.database import db
from hqai.core.logger import log
from hqai.history.downloader import HistoryDownloader


class HistoryUpdater:

    def __init__(self):

        self.downloader = HistoryDownloader()

    ########################################################

    def last_date(
        self,
        symbol: str,
    ):

        sql = f"""
        SELECT last_date
        FROM history_index
        WHERE symbol='{symbol}'
        """

        df = db.query(sql)

        if len(df) == 0:

            return None

        return df["last_date"][0]

    ########################################################

    def update_symbol(
        self,
        symbol: str,
    ):

        last = self.last_date(symbol)

        if last is None:

            log.warning(
                f"{symbol} has no history."
            )

            return

        start = pd.Timestamp(last) + timedelta(days=1)

        log.info(
            f"{symbol} update from {start.date()}"
        )

        # Download full history for now.
        # Next release will support incremental download.
        df = self.downloader.download_symbol(symbol)

        self.downloader.storage.save(
            df,
            symbol,
        )

        log.success(
            f"{symbol} updated."
        )

    ########################################################

    def update_all(self):

        universe = self.downloader.load_universe()

        symbols = universe["SYMBOL"].to_list()

        for symbol in symbols:

            self.update_symbol(symbol)