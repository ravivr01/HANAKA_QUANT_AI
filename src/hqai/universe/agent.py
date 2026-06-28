"""
HQAI Universe Agent
"""

from pathlib import Path

from hqai.core.config import config
from hqai.core.logger import log
from hqai.universe.downloader import UniverseDownloader


class UniverseAgent:
    """
    Downloads and prepares the NSE universe.
    """

    def __init__(self):

        self.universe = None

        self.output_dir = (
            config.data_dir /
            "bronze" /
            "universe"
        )

    def run(self):

        log.info("=" * 60)
        log.info("HQAI Universe Agent Started")
        log.info("=" * 60)

        self.prepare_directories()

        self.download_universe()

        log.info("=" * 60)
        log.info("Universe Agent Finished")
        log.info("=" * 60)

    def prepare_directories(self):

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        log.info(f"Directory Ready : {self.output_dir}")

    def download_universe(self):

        downloader = UniverseDownloader()

        self.universe = downloader.download()

        log.info(
            f"Universe Loaded : {len(self.universe)} stocks"
        )
