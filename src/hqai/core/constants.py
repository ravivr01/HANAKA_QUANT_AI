"""
HQAI Constants
"""

from pathlib import Path

# --------------------------------------------------
# Project
# --------------------------------------------------

PROJECT_NAME = "Hanaka Quant AI"
PROJECT_CODE = "HQAI"
VERSION = "0.1.0"

# --------------------------------------------------
# Exchange
# --------------------------------------------------

EXCHANGE = "NSE"

# --------------------------------------------------
# Database
# --------------------------------------------------

DATABASE_NAME = "hqai.duckdb"

# --------------------------------------------------
# File Extensions
# --------------------------------------------------

CSV = ".csv"
PARQUET = ".parquet"
JSON = ".json"

# --------------------------------------------------
# Date Formats
# --------------------------------------------------

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# --------------------------------------------------
# Data Layers
# --------------------------------------------------

BRONZE = "bronze"
SILVER = "silver"
GOLD = "gold"

# --------------------------------------------------
# Default Directories
# --------------------------------------------------

ROOT = Path.cwd()

DATA = ROOT / "data"
DATABASE = ROOT / "database"
LOGS = ROOT / "logs"
REPORTS = ROOT / "reports"
