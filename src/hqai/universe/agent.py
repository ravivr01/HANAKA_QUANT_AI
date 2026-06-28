"""
============================================================
HQAI Universe Agent
============================================================
Release : 0.3
============================================================
"""

from datetime import datetime

from hqai.core.config import config
from hqai.core.logger import log
from hqai.universe.downloader import UniverseDownloader
from hqai.universe.storage import UniverseStorage


class UniverseAgent:
    """
    Orchestrates the complete Universe Synchronization process.

    Workflow

        Prepare Directories
                ↓
        Download Universe
                ↓
        Store Data
                ↓
        Finish
    """

    def __init__(self):

        self.start_time = datetime.now()

        self.universe = None

        self.output_dir = (
            config.data_dir /
            "bronze" /
            "universe"
        )

    ########################################################

    def run(self):

        log.info("=" * 60)
        log.info("HQAI Universe Agent Started")
        log.info("=" * 60)

        self.prepare_directories()

        self.download_universe()

        self.store_universe()

        self.finish()

    ########################################################

    def prepare_directories(self):

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        log.info(
            f"Directory Ready : {self.output_dir}"
        )

    ########################################################

    def download_universe(self):

        downloader = UniverseDownloader()

        self.universe = downloader.download()

        log.info(
            f"Universe Loaded : {len(self.universe)} Stocks"
        )

    ########################################################

    def store_universe(self):

        storage = UniverseStorage()

        storage.save(self.universe)

    ########################################################

    def finish(self):

        elapsed = datetime.now() - self.start_time

        log.info("=" * 60)
        log.info("Universe Agent Finished")
        log.info(f"Elapsed Time : {elapsed}")
        log.info("=" * 60)
