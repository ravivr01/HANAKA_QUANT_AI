"""
==========================================================
HQAI Indicator Agent
==========================================================

Runs all registered indicators.

Author  : Ravi Varma
Release : 0.9
"""

from __future__ import annotations

import pandas as pd

from hqai.core.base_agent import BaseAgent
from hqai.core.logger import log
from hqai.indicators.registry import registry


class IndicatorAgent(BaseAgent):
    """
    Executes all registered indicators.
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

    ########################################################

    def sync(self):

        raise NotImplementedError("sync() will be implemented in Release 1.0")

    ########################################################

    def validate(self):

        raise NotImplementedError("validate() will be implemented in Release 1.0")

    ########################################################

    def summary(self):

        raise NotImplementedError("summary() will be implemented in Release 1.0")

    ########################################################

    def clean(self):

        raise NotImplementedError("clean() will be implemented in Release 1.0")
