# HQAI Database Design Document (DDD)

Version: 1.0

Project: Hanaka Quant AI

Author: Ravi Varma

---

# 1. Purpose

This document defines the logical and physical database architecture for HQAI.

DuckDB serves as the metadata repository.

Parquet serves as the analytical storage layer.

---

# 2. Storage Architecture

                HQAI

                    │

        DuckDB Metadata Layer

                    │

        Parquet Data Lake

                    │

      Bronze → Silver → Gold

---

# 3. Data Layers

## Bronze

Raw market data

Universe

History

Corporate Actions

Splits

Dividends

News

Options

Futures

Macros

---

## Silver

Cleaned datasets

Features

Indicators

Signals

Factor Models

---

## Gold

Strategies

Portfolio

Backtests

Risk

Machine Learning

Predictions

Reports

---

# 4. DuckDB Tables

history_index

feature_index

indicator_index

signal_index

strategy_index

portfolio_index

risk_index

prediction_index

universe

metadata

audit_log

---

# 5. Repository Pattern

Every engine owns one repository.

HistoryRepository

FeatureRepository

IndicatorRepository

SignalRepository

StrategyRepository

PortfolioRepository

Repositories never calculate.

Repositories only interact with DuckDB.

---

# 6. Storage Pattern

Every engine owns one storage class.

HistoryStorage

FeatureStorage

IndicatorStorage

SignalStorage

StrategyStorage

PortfolioStorage

Storage classes only read/write Parquet.

---

# 7. Index Tables

Every index contains

symbol

rows

first_date

last_date

version

status

updated_at

checksum

---

# 8. Data Lifecycle

Download

↓

Validate

↓

Store Bronze

↓

Build Features

↓

Build Indicators

↓

Generate Signals

↓

Run Strategies

↓

Portfolio

↓

Machine Learning

↓

Reports

---

# 9. Versioning

Every dataset has

Version

Created

Updated

Source

Checksum

Status

---

# 10. Performance

Partition by Symbol

Parquet Compression = ZSTD

DuckDB Indexes

Lazy Loading

Batch Processing

Vectorized Execution

---

# 11. Backup Strategy

Daily Backup

Weekly Snapshot

Monthly Archive

---

# 12. Error Recovery

Validation

Retry

Audit Log

Repair

Rebuild

---

# 13. Future Expansion

PostgreSQL

ClickHouse

Snowflake

Delta Lake

Cloud Storage

Distributed Computing