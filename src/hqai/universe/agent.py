"""
============================================================
HQAI Universe Agent
============================================================
Release : 0.3.0
Author  : Hanaka Quant AI
============================================================
"""

from datetime import datetime

from hqai.core.config import config
from hqai.core.logger import log

from hqai.universe.downloader import UniverseDownloader
from hqai.universe.validator import UniverseValidator
from hqai.universe.storage import UniverseStorage
from hqai.universe.metadata import UniverseMetadata


class UniverseAgent:
    """
    HQAI Universe Synchronization Pipeline

    Workflow

        Prepare Directories
                ↓
        Download Universe
                ↓
        Validate Universe
                ↓
        Store Universe
                ↓
        Generate Metadata
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

        self.downloader = UniverseDownloader()

        self.validator = UniverseValidator()

        self.storage = UniverseStorage()

        self.metadata = UniverseMetadata()

    ############################################################

    def run(self):

        log.info("=" * 60)
        log.info("HQAI Universe Synchronization Started")
        log.info("=" * 60)

        self.prepare_directories()

        self.download()

        self.validate()

        self.store()

        self.generate_metadata()

        self.finish()

    ############################################################

    def prepare_directories(self):

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        log.info(
            f"Directory Ready : {self.output_dir}"
        )

    ############################################################

    def download(self):

        self.universe = self.downloader.download()

        log.info(
            f"Downloaded : {len(self.universe)} records"
        )

    ############################################################

    def validate(self):

        self.universe = self.validator.validate(
            self.universe
        )

        log.info(
            f"Validated : {len(self.universe)} records"
        )

    ############################################################

    def store(self):

        self.storage.save(
            self.universe
        )

        log.info(
            "Universe Stored Successfully"
        )

    ############################################################

    def generate_metadata(self):

        self.metadata.generate(
            self.universe
        )

    ############################################################

    def finish(self):

        elapsed = datetime.now() - self.start_time

        log.info("=" * 60)
        log.info("HQAI Universe Synchronization Completed")
        log.info(f"Elapsed Time : {elapsed}")
        log.info("=" * 60)
