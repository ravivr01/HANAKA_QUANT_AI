"""
==========================================================
HQAI Indicator Metadata
==========================================================

Defines the metadata model used by every indicator.

Release : 0.8
Author  : Hanaka Quant AI

Every indicator must expose a complete metadata object.
"""

from __future__ import annotations

from dataclasses import dataclass, field

###############################################################################


@dataclass(slots=True)
class IndicatorMetadata:
    """
    Metadata describing an indicator.

    This object is used by:

    • Registry
    • CLI
    • Documentation
    • Knowledge Hub
    • Validation
    • AI Feature Store
    """

    ############################################################

    name: str

    ############################################################

    category: str

    ############################################################

    version: str

    ############################################################

    description: str

    ############################################################

    formula: str

    ############################################################

    reference: str

    ############################################################

    author: str

    ############################################################

    required_columns: list[str]

    ############################################################

    output_columns: list[str]

    ############################################################

    parameters: dict = field(default_factory=dict)

    ############################################################

    warmup_period: int = 0

    ############################################################

    complexity: str = "O(n)"

    ############################################################

    supports_incremental: bool = True

    ############################################################

    def summary(self) -> dict:

        return {
            "name": self.name,
            "category": self.category,
            "version": self.version,
            "warmup": self.warmup_period,
            "outputs": self.output_columns,
        }
