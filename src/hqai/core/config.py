"""
HQAI Configuration Manager
--------------------------
Central configuration for the Hanaka Quant AI platform.
"""

from pathlib import Path
from dataclasses import dataclass


# ==========================================================
# Project Information
# ==========================================================

PROJECT_NAME = "Hanaka Quant AI"
PROJECT_CODE = "HQAI"
VERSION = "0.1.0"


# ==========================================================
# Directory Structure
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[3]

SRC_DIR = ROOT_DIR / "src"
DATA_DIR = ROOT_DIR / "data"
DATABASE_DIR = ROOT_DIR / "database"
LOG_DIR = ROOT_DIR / "logs"
REPORT_DIR = ROOT_DIR / "reports"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

DUCKDB_FILE = DATABASE_DIR / "hqai.duckdb"


# ==========================================================
# Download Configuration
# ==========================================================

START_DATE = "2005-01-01"

MAX_WORKERS = 12

REQUEST_TIMEOUT = 30

MAX_RETRIES = 3


# ==========================================================
# Display Options
# ==========================================================

SHOW_PROGRESS = True

SHOW_ETA = True

SHOW_SPEED = True

SHOW_CPU = True

SHOW_RAM = True


# ==========================================================
# Configuration Object
# ==========================================================

@dataclass
class HQAIConfig:

    project_name: str = PROJECT_NAME
    version: str = VERSION

    root_dir: Path = ROOT_DIR
    data_dir: Path = DATA_DIR
    database_dir: Path = DATABASE_DIR
    log_dir: Path = LOG_DIR

    bronze_dir: Path = BRONZE_DIR
    silver_dir: Path = SILVER_DIR
    gold_dir: Path = GOLD_DIR

    duckdb_file: Path = DUCKDB_FILE

    start_date: str = START_DATE

    max_workers: int = MAX_WORKERS
    timeout: int = REQUEST_TIMEOUT
    retries: int = MAX_RETRIES


config = HQAIConfig()
