from pathlib import Path

from hqai.features.config import feature_config

history = set()

# Flat files
for file in feature_config.HISTORY_DIR.glob("*.parquet"):
    history.add(file.stem)

# Nested files
for file in feature_config.HISTORY_DIR.glob("*/history.parquet"):
    history.add(file.parent.name)

features = {
    f.stem
    for f in feature_config.FEATURE_DIR.glob("*.parquet")
}

missing = sorted(history - features)
extra = sorted(features - history)

print("=" * 60)
print("HQAI FEATURE VERIFICATION")
print("=" * 60)

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