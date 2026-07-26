"""
==========================================================
HQAI Indicator Configuration
==========================================================

Configuration for the Indicator Engine.

Author  : Ravi Varma
Version : 0.9.0
==========================================================
"""

from pathlib import Path

from hqai.core.config import config


class IndicatorConfig:
    """
    Indicator Engine Configuration
    """

    VERSION = "0.9.0"

    # --------------------------------------------------
    # Input
    # --------------------------------------------------

    FEATURE_DIR: Path = (
        config.data_dir
        / "silver"
        / "features"
    )

    # --------------------------------------------------
    # Output
    # --------------------------------------------------

    INDICATOR_DIR: Path = (
        config.data_dir
        / "gold"
        / "indicators"
    )

    METADATA_DIR: Path = (
        INDICATOR_DIR
        / "metadata"
    )

    # --------------------------------------------------
    # Default Periods
    # --------------------------------------------------

    SMA_PERIODS = (5, 10, 20, 50, 100, 200)

    EMA_PERIODS = (5, 10, 20, 50, 100, 200)

    RSI_PERIOD = 14

    MACD_FAST = 12

    MACD_SLOW = 26

    MACD_SIGNAL = 9

    BOLLINGER_PERIOD = 20

    BOLLINGER_STD = 2

    ATR_PERIOD = 14

    ADX_PERIOD = 14

    STOCH_PERIOD = 14

    STOCH_SMOOTH = 3

    VWAP_PERIOD = 20

    MIN_ROWS = 250

    COMPRESSION = "zstd"

    # --------------------------------------------------
    # Create Directories
    # --------------------------------------------------

    def __init__(self):

        self.INDICATOR_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.METADATA_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )


indicator_config = IndicatorConfig()