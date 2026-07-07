"""
==========================================================
HQAI History Agent
==========================================================

Coordinates the complete history download workflow.

Author  : Ravi Varma
Version : 1.0
"""

from __future__ import annotations

from datetime import datetime

from hqai.core.logger import log
from hqai.history.downloader import HistoryDownloader


class HistoryAgent:

    """
    Main History Orchestrator.
    """

    def __init__(self):

        self.downloader = HistoryDownloader()

    ########################################################

    def sync(self):

        start = datetime.now()

        log.info("=" * 60)
        log.info("HQAI HISTORY SYNCHRONIZATION")
        log.info("=" * 60)

        failed = self.downloader.download_all()

        end = datetime.now()

        elapsed = end - start

        log.info("=" * 60)
        log.success("Synchronization Finished")
        log.info(f"Elapsed : {elapsed}")
        log.warning(f"Failed  : {len(failed)}")

        if failed:

            log.warning("Failed Symbols")

            for symbol in failed:

                log.warning(symbol)

        return failed

    ########################################################

    def sync_symbol(
        self,
        symbol: str,
    ):

        log.info(f"Synchronizing {symbol}")

        df = self.downloader.download_symbol(symbol)

        self.downloader.storage.save(df, symbol)

        self.downloader.storage.register(symbol)

        log.success(f"{symbol} synchronized")

    ########################################################

    def health(self):

        universe = self.downloader.load_universe()

        log.info("=" * 60)

        log.info(f"Universe Size : {len(universe)}")

        log.info("=" * 60)