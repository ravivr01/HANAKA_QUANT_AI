"""
==========================================================
HQAI History Statistics
==========================================================

Author  : Ravi Varma
Version : 0.7.2
"""

from pathlib import Path
import duckdb

from hqai.core.config import config


class HistoryStats:

    def __init__(self):

        self.history_dir = config.data_dir / "bronze" / "history"

        self.db = duckdb.connect(str(config.duckdb_file))

    # -----------------------------------------------------

    def universe_count(self):

        return self.db.execute(
            "SELECT COUNT(*) FROM universe"
        ).fetchone()[0]

    # -----------------------------------------------------

    def indexed_count(self):

        try:

            return self.db.execute(
                "SELECT COUNT(*) FROM history_index"
            ).fetchone()[0]

        except:

            return 0

    # -----------------------------------------------------

    def history_files(self):

        return list(self.history_dir.rglob("*.parquet"))

    # -----------------------------------------------------

    def history_count(self):

        return len(self.history_files())

    # -----------------------------------------------------

    def disk_usage(self):

        return sum(
            f.stat().st_size
            for f in self.history_files()
        )

    # -----------------------------------------------------

    def format_size(self, size):

        for unit in ["B", "KB", "MB", "GB", "TB"]:

            if size < 1024:

                return f"{size:.2f} {unit}"

            size /= 1024

        return f"{size:.2f} PB"

    # -----------------------------------------------------

    def largest_file(self):

        files = self.history_files()

        if not files:

            return None

        return max(files, key=lambda x: x.stat().st_size)

    # -----------------------------------------------------

    def smallest_file(self):

        files = self.history_files()

        if not files:

            return None

        return min(files, key=lambda x: x.stat().st_size)

    # -----------------------------------------------------

    def database_health(self):

        try:

            self.db.execute("SELECT 1")

            return "Healthy"

        except:

            return "FAILED"

    # -----------------------------------------------------

    def run(self):

        universe = self.universe_count()

        indexed = self.indexed_count()

        files = self.history_files()

        history = len(files)

        missing = max(universe - indexed, 0)

        extra = max(history - universe, 0)

        print()

        print("=" * 70)

        print("               HQAI HISTORY STATISTICS")

        print("=" * 70)

        print()

        print("GENERAL")

        print("-" * 70)

        print(f"History Folder      : {self.history_dir}")

        print(f"Folder Exists       : {self.history_dir.exists()}")

        print()

        print("COUNTS")

        print("-" * 70)

        print(f"Universe Symbols    : {universe}")

        print(f"Indexed Symbols     : {indexed}")

        print(f"History Files       : {history}")

        print(f"Missing Symbols     : {missing}")

        print(f"Extra Files         : {extra}")

        print()

        print("STORAGE")

        print("-" * 70)

        print(f"Disk Usage          : {self.format_size(self.disk_usage())}")

        largest = self.largest_file()

        smallest = self.smallest_file()

        if largest:

            print(
                f"Largest File        : "
                f"{largest.relative_to(self.history_dir)} "
                f"({self.format_size(largest.stat().st_size)})"
            )

        if smallest:

            print(
                f"Smallest File       : "
                f"{smallest.relative_to(self.history_dir)} "
                f"({self.format_size(smallest.stat().st_size)})"
            )

        print()

        print("DATABASE")

        print("-" * 70)

        print(f"DuckDB Status       : {self.database_health()}")

        print()

        print("SAMPLE FILES")

        print("-" * 70)

        for file in files[:10]:

            print(file.relative_to(self.history_dir))

        print()

        print("=" * 70)