"""
==========================================================
HQAI Feature Configuration
==========================================================

Central configuration for the HQAI Feature Engine.

Author  : Ravi Varma
Version : 0.8.1
==========================================================
"""

from pathlib import Path

from hqai.core.config import config


class FeatureConfig:
    """
    Feature Engine Configuration
    """

    VERSION = "0.8.1"

    # --------------------------------------------------
    # Input
    # --------------------------------------------------

    HISTORY_DIR: Path = (
        config.data_dir
        / "bronze"
        / "history"
    )

    # --------------------------------------------------
    # Output
    # --------------------------------------------------

    FEATURE_DIR: Path = (
        config.data_dir
        / "silver"
        / "features"
    )

    METADATA_DIR: Path = (
        FEATURE_DIR
        / "metadata"
    )

    # --------------------------------------------------
    # Rolling Windows
    # --------------------------------------------------

    WINDOWS = (
        5,
        10,
        20,
        50,
        100,
        200,
    )

    # --------------------------------------------------
    # Minimum history required
    # --------------------------------------------------

    MIN_ROWS = 250

    # --------------------------------------------------
    # Parquet Compression
    # --------------------------------------------------

    COMPRESSION = "zstd"

    # --------------------------------------------------
    # Create Directories
    # --------------------------------------------------

    def __init__(self):

        self.FEATURE_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.METADATA_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )


feature_config = FeatureConfig()