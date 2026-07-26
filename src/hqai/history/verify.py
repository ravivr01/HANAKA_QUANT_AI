"""
==========================================================
HQAI History Verification
==========================================================
"""

from pathlib import Path

import duckdb

from hqai.core.config import config


class HistoryVerify:

    def __init__(self):

        self.history_dir = config.data_dir / "bronze" / "history"

        self.db = duckdb.connect(str(config.duckdb_file))

    # -------------------------------------------------

    def universe(self):

        rows = self.db.execute("""
            SELECT SYMBOL
            FROM universe
        """).fetchall()

        return {r[0] for r in rows}

    # -------------------------------------------------

    def history(self):

        symbols = set()

        for file in self.history_dir.rglob("*.parquet"):

            if file.name == "history.parquet":

                symbols.add(file.parent.name)

            else:

                symbols.add(file.stem)

        return symbols

    # -------------------------------------------------

    def verify(self):

        universe = self.universe()

        history = self.history()

        missing = sorted(universe - history)

        extra = sorted(history - universe)

        print()

        print("=" * 70)

        print("HQAI HISTORY VERIFICATION")

        print("=" * 70)

        print()

        print(f"Universe Symbols : {len(universe)}")

        print(f"History Symbols  : {len(history)}")

        print(f"Missing Symbols  : {len(missing)}")

        print(f"Extra Symbols    : {len(extra)}")

        print()

        if missing:

            print("First 10 Missing")

            for s in missing[:10]:

                print(" ", s)

            print()

        if extra:

            print("First 10 Extra")

            for s in extra[:10]:

                print(" ", s)

            print()

        if not missing and not extra:

            print("STATUS : PASS")

        else:

            print("STATUS : WARNING")

        print()

        print("=" * 70)