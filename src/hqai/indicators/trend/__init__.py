"""
HQAI Trend Indicators
"""

from hqai.indicators.registry import registry

from .sma import SMA

registry.register(SMA)

__all__ = [
    "SMA",
]