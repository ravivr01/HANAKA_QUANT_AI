"""
HQAI Database Manager
Release : 0.3
Author  : Hanaka Quant AI

Central database layer for the entire HQAI platform.
Every module must communicate with DuckDB through this class.
"""

from pathlib import Path
from typing import Optional

import duckdb
import polars as pl

from hqai.core.config import config
from hqai.core.logger import log


class DatabaseManager:
    """
    HQAI Central Database Manager

    Responsibilities
    ----------------
    - Create database
    - Open connection
    - Execute SQL
    - Query data
    - Register Parquet files
    - Check tables
    - Backup database
    - Close connection
    """

    def __init__(self):

        self.db_path: Path = config.duckdb_file

        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        self.connection: Optional[duckdb.DuckDBPyConnection] = None

        self.connect()

        self.create_schema()

        self.create_history_index()

    ########################################################

    def connect(self):

        if self.connection is None:

            self.connection = duckdb.connect(str(self.db_path))

            log.info(f"Connected -> {self.db_path}")

    ########################################################

    def disconnect(self):

        if self.connection:

            self.connection.close()

            self.connection = None

            log.info("Database connection closed")

    ########################################################

    def execute(self, sql: str):

        return self.connection.execute(sql)

    ########################################################

    def query(self, sql: str) -> pl.DataFrame:

        return self.connection.sql(sql).pl()

    ########################################################

    def table_exists(self, table_name: str) -> bool:

        sql = f"""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name='{table_name}'
        """

        return self.connection.execute(sql).fetchone()[0] > 0

    ########################################################

    def register_parquet(self, view_name: str, parquet_file: str):

        sql = f"""
        CREATE OR REPLACE VIEW {view_name}
        AS
        SELECT *
        FROM read_parquet('{parquet_file}')
        """

        self.execute(sql)

    ########################################################

    def create_schema(self):

        self.execute("""
        CREATE SCHEMA IF NOT EXISTS bronze;

        CREATE SCHEMA IF NOT EXISTS silver;

        CREATE SCHEMA IF NOT EXISTS gold;
        """)

        log.info("Database schema created")

    ########################################################

    def create_history_index(self):

        self.execute("""
        CREATE TABLE IF NOT EXISTS history_index (

            symbol VARCHAR PRIMARY KEY,

            rows BIGINT,

            first_date DATE,

            last_date DATE,

            updated_at TIMESTAMP,

            status VARCHAR

        )
        """)

        log.info("History Index created")

    ########################################################

    def backup(self, filename: str):

        self.execute(f"EXPORT DATABASE '{filename}'")

        log.info(f"Backup created -> {filename}")

    ########################################################

    def health_check(self) -> bool:

        try:

            self.connection.execute("SELECT 1")

            return True

        except Exception as e:

            log.error(e)

            return False


db = DatabaseManager()