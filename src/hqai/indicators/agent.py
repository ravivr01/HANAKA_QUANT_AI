"""
==========================================================
HQAI Indicator Agent
==========================================================

Runs all registered indicators.

Author  : Ravi Varma
Release : F1.2
"""

from __future__ import annotations

import pandas as pd

from hqai.core.logger import log
from hqai.indicators.registry import registry


class IndicatorAgent:

    """
    Executes HQAI indicators.
    """

    ########################################################

    def build(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        result = df.copy()

        for name in registry.list():

            log.info(f"Running {name}")

            indicator = registry.get(name)()

            result = indicator.run(result)

        return result