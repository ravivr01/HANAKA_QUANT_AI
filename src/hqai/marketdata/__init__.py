"""
==========================================================
HQAI Market Data Package
Release : R-005-001
Author  : Hanaka Quant AI

Initializes the Market Data package and registers
all available providers.
==========================================================
"""

# Import provider modules so they self-register
import hqai.marketdata.providers.yahoo  # noqa: F401

from hqai.marketdata.agent import MarketDataAgent
from hqai.marketdata.registry import registry

__all__ = [
    "MarketDataAgent",
    "registry",
]
