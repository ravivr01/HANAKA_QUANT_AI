#!/bin/bash

clear

echo "=============================================="
echo "      HANAKA QUANT AI v1.0"
echo "=============================================="
echo

echo "[1/5] Checking Python..."

python3 --version

echo
echo "[2/5] Checking Virtual Environment..."

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "❌ Virtual Environment NOT Active"
    exit 1
fi

echo "✅ Virtual Environment Active"

echo
echo "[3/5] Checking Project Structure..."

folders=(
agents
config
dashboard
database
data
features
indicators
logs
models
reports
scripts
utils
)

for folder in "${folders[@]}"
do
    if [ -d "$folder" ]; then
        echo "✅ $folder"
    else
        echo "❌ Missing $folder"
    fi
done

echo
echo "[4/5] Checking Python Packages..."

python3 -c "import pandas, duckdb, yfinance" >/dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Required packages installed"
else
    echo "❌ Missing packages"
fi

echo
echo "[5/5] Bootstrap Completed Successfully"