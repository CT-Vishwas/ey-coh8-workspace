1. Architecture
Layered, script-orchestrated batch pipeline:
```text
┌─────────────┐   ┌──────────────┐   ┌───────────────┐   ┌────────────────┐   ┌────────────────┐
│  Ingestion   │→ │  Validation/  │→ │   SQLite       │→ │   Analysis      │→ │   Reporting     │
│  (CSV read,  │   │  Cleaning     │   │   Loader       │   │   (pandas)      │   │   (matplotlib   │
│  chunked)    │   │  (schema,     │   │   (indexed     │   │   metrics/      │   │   + Jinja2      │
│              │   │  dtype, dup)  │   │   tables)      │   │   aggregations  │   │   HTML)         │
└─────────────┘   └──────────────┘   └───────────────┘   └────────────────┘   └────────────────┘
        │                  │                  │                   │                     │
        └──────────────────┴──── central logging + config ────────┴─────────────────────┘
```
Orchestration: a single main.py driving stages in sequence; each stage is an independent, testable module with a clear input/output contract.
Config-driven: paths, DB name, chunk size controlled via config.yaml — no hardcoded paths.
Idempotent runs: timestamped report/chart folders per run; DB load designed so re-running with the same CSV doesn't duplicate rows.
Stateless analysis layer: pandas reads from SQLite (not CSV directly) so SQLite is the single source of truth.
Data status: sales (2,500 rows) and customers (1,000 rows) now share 920 overlapping Customer_IDs with 0 unmatched sales rows — validated and confirmed working for joins.

2. Project Structure

```text
reporting_app/
├── config/
│   └── config.yaml                # paths, chunk size, DB name, thresholds
├── data/
│   ├── sales_data-2.csv
│   └── customers_data.csv
├── db/
│   └── reporting.db                # SQLite database (generated)
├── src/
│   ├── __init__.py
│   ├── config.py                    # config loader (path resolution)
│   ├── ingestion.py                # chunked CSV readers, dtype schemas
│   ├── validation.py                # schema checks, null/dup/range checks, quarantine bad rows
│   ├── db_loader.py                 # table DDL, indexes, bulk insert
│   ├── analysis.py                  # pandas aggregations (revenue, trends, top products, etc.)
│   ├── visualization.py             # matplotlib chart functions, saved as PNG
│   ├── report_builder.py            # Jinja2 template rendering → HTML
│   └── utils/
│       ├── __init__.py
│       ├── logging_config.py        # centralized logger setup
│       └── db_utils.py              # connection context manager, PRAGMAs
├── templates/
│   └── report_template.html         # Jinja2 HTML template + embedded CSS
├── output/
│   ├── charts/                      # generated PNGs per run
│   ├── reports/                     # report_<timestamp>.html
│   └── rejected/                    # quarantined bad rows
├── logs/
│   └── pipeline_<date>.log
├── tests/
│   ├── test_ingestion.py
│   ├── test_validation.py
│   ├── test_analysis.py
│   └── test_db_loader.py
├── main.py                          # CLI entry point / orchestrator
├── requirements.txt
└── README.md
```

3. Data Flow
Extract: ingestion.py reads both CSVs using pandas.read_csv(..., chunksize=N, dtype={...}, parse_dates=['Date']).
Validate/Clean (validation.py), per chunk: required-column check; type coercion with quarantine of failing rows (→ output/rejected/, not silently dropped); duplicate Transaction_ID/Customer_ID detection; domain checks (Quantity > 0, Total_Amount ≈ Quantity × Unit_Price); referential check on sales.Customer_ID vs customers.Customer_ID.
Load (db_loader.py): cleaned chunks appended via to_sql(..., if_exists='append', method='multi'); indexes created after bulk load; ANALYZE run afterward.
Transform/Analyze (analysis.py): aggregation pushed to SQL where possible; small aggregated results pulled into pandas.
Visualize (visualization.py): each analysis result → dedicated matplotlib chart saved as PNG.
Report (report_builder.py): Jinja2 combines KPI cards, tables, and embedded charts into one HTML file.
Log throughout: row counts, rejects, timing per stage, final report path.

4. Database Tables
```text
customers                              sales
────────────────────────               ─────────────────────────────
customer_id   TEXT PRIMARY KEY         transaction_id   TEXT PRIMARY KEY
name          TEXT                     txn_date         TEXT (ISO 8601), indexed
age           INTEGER                  customer_id      TEXT   (FK)
gender        TEXT                     product_category TEXT
location      TEXT                     product_name     TEXT
total_spent   REAL                     quantity         INTEGER
                                       unit_price       REAL
                                       total_amount     REAL
                                       payment_method   TEXT
                                       load_batch_id    TEXT   (audit column)

data_quality_log                       load_audit
────────────────────────               ─────────────────────────
id            INTEGER PK AUTOINCREMENT batch_id       TEXT PRIMARY KEY
run_id        TEXT                     source_file    TEXT
table_name    TEXT                     rows_read      INTEGER
issue_type    TEXT                     rows_loaded    INTEGER
row_ref       TEXT                     rows_rejected  INTEGER
detail        TEXT                     started_at     TEXT
created_at    TEXT                     finished_at    TEXT
```

Indexes:

sales: PRIMARY KEY(transaction_id), idx_sales_customer_id(customer_id), idx_sales_date(txn_date), idx_sales_category(product_category), composite idx_sales_date_category(txn_date, product_category).
customers: PRIMARY KEY(customer_id).
PRAGMA journal_mode=WAL, synchronous=NORMAL, temp_store=MEMORY during bulk load; indexes built after load.

5. Analysis and Reporting
Revenue KPIs: total revenue, total transactions, average order value, average items/transaction.
Time trend: daily/weekly/monthly revenue and transaction counts.
Category performance: revenue & quantity by Product_Category, top 10 Product_Name by revenue.
Payment method mix: transaction count/revenue share by Payment_Method.
Customer insights (now join-able): revenue by age band, gender, location; top customers by spend; matched-vs-unmatched sales metric (now 0% unmatched).
Data quality summary: rows rejected, Total_Amount mismatches — surfaced in its own report section.

6. HTML Report Structure

```text
1. Header             – title, generation timestamp, data date range, run id
2. Executive Summary  – KPI cards (revenue, transactions, AOV, unique customers)
3. Data Quality Panel – rows loaded/rejected, referential-integrity status
4. Sales Trends       – line chart (revenue over time), transactions over time
5. Category Analysis  – bar chart (revenue by category), top 10 products
6. Payment Methods    – pie/bar chart of payment method mix
7. Customer Insights  – bar chart (revenue by location), age distribution, gender split
8. Detailed Tables    – scrollable HTML tables (top products, category summary)
9. Footer             – pipeline version, config summary, log file reference
```
Charts embedded as base64 PNG (single-file portability); tables via styled DataFrame.to_html(classes="report-table"); responsive CSS, consistent color palette, print-friendly.

7. Error Handling and Logging
Centralized rotating-file + console logger (logging_config.py), structured format, INFO/WARNING/ERROR levels.
Per-stage try/except with specific exceptions (FileNotFoundError, sqlite3.IntegrityError, generic fallback with traceback).
Bad rows quarantined to CSV + data_quality_log table — never silently dropped.
Per-chunk DB transactions for resumability; load_audit table tracks batch status.
Non-zero exit code on stage failure (CI/scheduler friendly).

8. Performance Optimization
Chunked CSV reads with explicit dtype/parse_dates — bounds memory regardless of file size.
Bulk load via to_sql(method='multi') instead of row-by-row inserts.
Indexes created after bulk load; ANALYZE refreshes query-planner stats.
SQLite PRAGMAs tuned for write throughput during load.
Aggregation pushed to SQL; pandas only handles small, pre-aggregated result sets.
Matplotlib Agg backend, figures closed after saving, charts built from aggregated (not raw) data.