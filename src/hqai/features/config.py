"""
==========================================================
HQAI Feature Configuration
==========================================================
"""

from pathlib import Path

from hqai.core.config import config


class FeatureConfig:
    """
    Feature Engine Configuration
    """

    VERSION = "0.8.0"

    HISTORY_DIR = (
        config.data_dir
        / "bronze"
        / "history"
    )

    FEATURE_DIR = (
        config.data_dir
        / "silver"
        / "features"
    )

    FEATURE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    WINDOWS = [
        5,
        10,
        20,
        50,
        100,
        200,
    ]

    MIN_ROWS = 250


feature_config = FeatureConfig()