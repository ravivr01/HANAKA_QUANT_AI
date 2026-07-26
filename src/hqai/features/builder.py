"""
==========================================================
HQAI Feature Builder
==========================================================

Builds quantitative features from OHLCV history.

Author  : Ravi Varma
Version : 0.8.1
==========================================================
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from hqai.features.config import feature_config


class FeatureBuilder:
    """
    Generates quantitative features.
    """

    def __init__(self):

        self.windows = feature_config.WINDOWS

    # --------------------------------------------------
    # Build
    # --------------------------------------------------

    def build(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        data = df.copy()

        # ------------------------------------------
        # Basic Returns
        # ------------------------------------------

        data["RETURN"] = data["Close"].pct_change()

        data["LOG_RETURN"] = np.log(
            data["Close"] / data["Close"].shift(1)
        )

        # ------------------------------------------
        # Dollar Volume
        # ------------------------------------------

        data["DOLLAR_VOLUME"] = (

            data["Close"]

            * data["Volume"]

        )

        # ------------------------------------------
        # Rolling Mean
        # ------------------------------------------

        for window in self.windows:

            data[f"SMA_{window}"] = (

                data["Close"]

                .rolling(window)

                .mean()

            )

        # ------------------------------------------
        # Rolling Standard Deviation
        # ------------------------------------------

        data["STD_20"] = (

            data["RETURN"]

            .rolling(20)

            .std()

        )

        # ------------------------------------------
        # Historical Volatility
        # ------------------------------------------

        data["HIST_VOL_20"] = (

            data["STD_20"]

            * np.sqrt(252)

        )

        # ------------------------------------------
        # Z Score
        # ------------------------------------------

        rolling_mean = (

            data["Close"]

            .rolling(20)

            .mean()

        )

        rolling_std = (

            data["Close"]

            .rolling(20)

            .std()

        )

        data["ZSCORE_20"] = (

            data["Close"] - rolling_mean

        ) / rolling_std

        # ------------------------------------------
        # True Range
        # ------------------------------------------

        high_low = (

            data["High"]

            - data["Low"]

        )

        high_close = (

            data["High"]

            - data["Close"].shift()

        ).abs()

        low_close = (

            data["Low"]

            - data["Close"].shift()

        ).abs()

        data["TRUE_RANGE"] = pd.concat(

            [

                high_low,

                high_close,

                low_close,

            ],

            axis=1,

        ).max(axis=1)

        # ------------------------------------------
        # ATR 14
        # ------------------------------------------

        data["ATR_14"] = (

            data["TRUE_RANGE"]

            .rolling(14)

            .mean()

        )

        return data