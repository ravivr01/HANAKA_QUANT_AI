"""
============================================================
HQAI Filesystem Manager
============================================================

Centralized management of all HQAI directories.

Release : 0.4.0
============================================================
"""

from __future__ import annotations

from pathlib import Path

from hqai.core.config import config
from hqai.core.logger import log


class FileSystem:
    """
    Centralized filesystem manager.

    Every HQAI module should use this class instead
    of creating directories manually.
    """

    def __init__(self):

        self.root = config.root_dir

        self.directories = {
            "data": config.data_dir,
            "database": config.database_dir,
            "logs": config.log_dir,

            "bronze": config.data_dir / "bronze",
            "silver": config.data_dir / "silver",
            "gold": config.data_dir / "gold",

            "bronze_universe": config.data_dir / "bronze" / "universe",
            "bronze_history": config.data_dir / "bronze" / "history",

            "silver_history": config.data_dir / "silver" / "history",
            "silver_indicators": config.data_dir / "silver" / "indicators",

            "gold_features": config.data_dir / "gold" / "features",
            "gold_models": config.data_dir / "gold" / "models",
            "gold_reports": config.data_dir / "gold" / "reports",
        }

    ########################################################

    def initialize(self) -> None:
        """
        Create all HQAI directories.
        """

        log.info("Initializing filesystem...")

        for directory in self.directories.values():

            directory.mkdir(
                parents=True,
                exist_ok=True,
            )

        log.info("Filesystem initialized successfully.")

    ########################################################

    def get(self, name: str) -> Path:
        """
        Return a directory path by name.
        """

        if name not in self.directories:
            raise KeyError(
                f"Unknown directory: {name}"
            )

        return self.directories[name]

    ########################################################

    def exists(self, name: str) -> bool:
        """
        Check whether a managed directory exists.
        """

        return self.get(name).exists()

    ########################################################

    def list_directories(self) -> dict[str, Path]:
        """
        Return all managed directories.
        """

        return self.directories.copy()


filesystem = FileSystem()
