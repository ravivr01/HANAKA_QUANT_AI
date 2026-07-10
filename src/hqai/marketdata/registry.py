"""
==========================================================
HQAI Provider Registry
Release : R-005-001
Author  : Hanaka Quant AI

Central registry for Market Data Providers.
==========================================================
"""

from __future__ import annotations

from typing import Type

from hqai.marketdata.base import BaseProvider


class ProviderRegistry:
    """
    Registry for all Market Data Providers.

    Examples
    --------
    registry.register("yahoo", YahooProvider)

    Provider = registry.get("yahoo")

    provider = Provider()
    """

    ########################################################

    def __init__(self):

        self._providers: dict[str, Type[BaseProvider]] = {}

    ########################################################

    def register(
        self,
        name: str,
        provider: Type[BaseProvider],
    ) -> None:

        key = name.lower().strip()

        if key in self._providers:

            raise ValueError(f"Provider '{name}' already registered.")

        self._providers[key] = provider

    ########################################################

    def unregister(
        self,
        name: str,
    ) -> None:

        key = name.lower().strip()

        self._providers.pop(key, None)

    ########################################################

    def get(
        self,
        name: str,
    ) -> Type[BaseProvider]:

        key = name.lower().strip()

        if key not in self._providers:

            available = ", ".join(self.list())

            raise ValueError(f"Unknown provider '{name}'. " f"Available: [{available}]")

        return self._providers[key]

    ########################################################

    def exists(
        self,
        name: str,
    ) -> bool:

        return name.lower().strip() in self._providers

    ########################################################

    def list(
        self,
    ) -> list[str]:

        return sorted(self._providers.keys())

    ########################################################

    def count(
        self,
    ) -> int:

        return len(self._providers)

    ########################################################

    def clear(
        self,
    ) -> None:

        self._providers.clear()


registry = ProviderRegistry()
