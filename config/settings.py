cat > config/settings.py << 'EOF'
"""
HANAKA QUANT AI
Global Settings
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
CSV_DIR = DATA_DIR / "csv"
PARQUET_DIR = DATA_DIR / "parquet"
CACHE_DIR = DATA_DIR / "cache"
TEMP_DIR = DATA_DIR / "temp"

DATABASE_DIR = PROJECT_ROOT / "database"
DUCKDB_DIR = DATABASE_DIR / "duckdb"
DUCKDB_FILE = DUCKDB_DIR / "hanaka_quant.duckdb"

REPORT_DIR = PROJECT_ROOT / "reports"
LOG_DIR = PROJECT_ROOT / "logs"

START_DATE = "2010-01-01"
MAX_WORKERS = 12
REQUEST_TIMEOUT = 30
RETRY_COUNT = 3

SAVE_CSV = True
SAVE_PARQUET = True
SAVE_DUCKDB = True

SHOW_PROGRESS = True
SHOW_ETA = True
SHOW_SPEED = True
SHOW_CPU = True
SHOW_RAM = True
EOF