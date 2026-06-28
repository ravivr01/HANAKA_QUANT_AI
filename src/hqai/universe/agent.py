"""
HQAI Universe Agent
"""
from hqai.universe.downloader import UniverseDownloader
from hqai.core.logger import log


class UniverseAgent:
    """
    Downloads and prepares the NSE universe.
    """

    def run(self):

        log.info("=" * 60)
        log.info("HQAI Universe Agent Started")
        log.info("=" * 60)

        print()
        print("Universe Agent Started")
        print("Step 1 : Agent Loaded Successfully")
        print()
