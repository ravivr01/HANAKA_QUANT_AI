"""
==========================================================
HQAI Indicator Registry
==========================================================

Central registry for all indicators.

Author  : Ravi Varma
Release : F1
"""

from __future__ import annotations

from typing import Type

from hqai.indicators.base import BaseIndicator


class IndicatorRegistry:
    """
    Central registry for HQAI indicators.
    """

    def __init__(self):

        self._registry: dict[str, Type[BaseIndicator]] = {}

    ########################################################

    def register(
        self,
        indicator: Type[BaseIndicator],
    ) -> None:

        self._registry[indicator.__name__] = indicator

    ########################################################

    def get(
        self,
        name: str,
    ) -> Type[BaseIndicator]:

        return self._registry[name]

    ########################################################

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._registry

    ########################################################

    def list(self) -> list[str]:

        return sorted(self._registry.keys())

    ########################################################

    def count(self) -> int:

        return len(self._registry)


registry = IndicatorRegistry()
