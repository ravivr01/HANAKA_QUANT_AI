"""
==========================================================
HQAI Feature CLI
==========================================================
"""

from pathlib import Path

import typer

from hqai.features.agent import FeatureAgent
from hqai.features.storage import FeatureStorage
from hqai.features.config import feature_config

app = typer.Typer(
    help="Feature Management Commands"
)


# ---------------------------------------------------------
# Build
# ---------------------------------------------------------

@app.command("build")
def build():

    FeatureAgent().run()


# ---------------------------------------------------------
# Verify
# ---------------------------------------------------------

@app.command("verify")
def verify():

    history = set()

    # Flat files
    for file in feature_config.HISTORY_DIR.glob("*.parquet"):
        history.add(file.stem)

    # Nested files
    for file in feature_config.HISTORY_DIR.glob("*/history.parquet"):
        history.add(file.parent.name)

    storage = FeatureStorage()

    features = set(storage.list_symbols())

    missing = sorted(history - features)

    extra = sorted(features - history)

    print()

    print("=" * 70)
    print("HQAI FEATURE VERIFICATION")
    print("=" * 70)

    print(f"History Files : {len(history)}")
    print(f"Feature Files : {len(features)}")
    print(f"Missing       : {len(missing)}")
    print(f"Extra         : {len(extra)}")

    if missing:

        print("\nMissing Symbols")

        for symbol in missing:

            print(symbol)

    if extra:

        print("\nExtra Symbols")

        for symbol in extra:

            print(symbol)

    print("=" * 70)


# ---------------------------------------------------------
# Statistics
# ---------------------------------------------------------

@app.command("stats")
def stats():

    storage = FeatureStorage()

    print()

    print("=" * 70)
    print("HQAI FEATURE STATISTICS")
    print("=" * 70)

    print(f"Directory      : {storage.feature_dir}")
    print(f"Feature Files  : {storage.count()}")
    print(f"Disk Usage MB  : {storage.disk_usage():.2f}")

    print("=" * 70)


# ---------------------------------------------------------
# Update
# ---------------------------------------------------------

@app.command("update")
def update():

    typer.echo("Feature Update - Coming Soon")