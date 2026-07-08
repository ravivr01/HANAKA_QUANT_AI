"""
==========================================================
HQAI Configuration Manager
==========================================================

Central configuration for the Hanaka Quant AI platform.

Author  : Ravi Varma
Release : 0.2.0
==========================================================
"""

from pathlib import Path
from dataclasses import dataclass, field

# ==========================================================
# Project Information
# ==========================================================

PROJECT_NAME = "Hanaka Quant AI"
PROJECT_CODE = "HQAI"
VERSION = "0.2.0"


# ==========================================================
# Directory Structure
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[3]

SRC_DIR = ROOT_DIR / "src"

DATA_DIR = ROOT_DIR / "data"

DATABASE_DIR = ROOT_DIR / "database"

LOG_DIR = ROOT_DIR / "logs"

REPORT_DIR = ROOT_DIR / "reports"

CONFIG_DIR = ROOT_DIR / "configs"

TEST_DIR = ROOT_DIR / "tests"

DOCS_DIR = ROOT_DIR / "docs"

KNOWLEDGE_DIR = ROOT_DIR / "knowledge"


# ==========================================================
# Data Lake
# ==========================================================

BRONZE_DIR = DATA_DIR / "bronze"

SILVER_DIR = DATA_DIR / "silver"

GOLD_DIR = DATA_DIR / "gold"


# ==========================================================
# Database
# ==========================================================

DUCKDB_FILE = DATABASE_DIR / "hqai.duckdb"


# ==========================================================
# Download Configuration
# ==========================================================

START_DATE = "2005-01-01"

DEFAULT_PERIOD = "10y"

DEFAULT_INTERVAL = "1d"

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

    # ------------------------------------------------------
    # Project
    # ------------------------------------------------------

    project_name: str = PROJECT_NAME

    project_code: str = PROJECT_CODE

    version: str = VERSION

    # ------------------------------------------------------
    # Directories
    # ------------------------------------------------------

    root_dir: Path = ROOT_DIR

    src_dir: Path = SRC_DIR

    data_dir: Path = DATA_DIR

    database_dir: Path = DATABASE_DIR

    log_dir: Path = LOG_DIR

    report_dir: Path = REPORT_DIR

    config_dir: Path = CONFIG_DIR

    docs_dir: Path = DOCS_DIR

    knowledge_dir: Path = KNOWLEDGE_DIR

    tests_dir: Path = TEST_DIR

    bronze_dir: Path = BRONZE_DIR

    silver_dir: Path = SILVER_DIR

    gold_dir: Path = GOLD_DIR

    # ------------------------------------------------------
    # Database
    # ------------------------------------------------------

    duckdb_file: Path = DUCKDB_FILE

    # ------------------------------------------------------
    # Download
    # ------------------------------------------------------

    start_date: str = START_DATE

    default_period: str = DEFAULT_PERIOD

    default_interval: str = DEFAULT_INTERVAL

    max_workers: int = MAX_WORKERS

    timeout: int = REQUEST_TIMEOUT

    retries: int = MAX_RETRIES

    # ------------------------------------------------------
    # Display
    # ------------------------------------------------------

    show_progress: bool = SHOW_PROGRESS

    show_eta: bool = SHOW_ETA

    show_speed: bool = SHOW_SPEED

    show_cpu: bool = SHOW_CPU

    show_ram: bool = SHOW_RAM

    # ------------------------------------------------------
    # Initialization
    # ------------------------------------------------------

    initialized: bool = field(init=False, default=False)

    def __post_init__(self):

        directories = [
            self.data_dir,
            self.database_dir,
            self.log_dir,
            self.report_dir,
            self.config_dir,
            self.docs_dir,
            self.knowledge_dir,
            self.tests_dir,
            self.bronze_dir,
            self.silver_dir,
            self.gold_dir,
        ]

        for directory in directories:

            directory.mkdir(
                parents=True,
                exist_ok=True,
            )

        self.initialized = True


config = HQAIConfig()
