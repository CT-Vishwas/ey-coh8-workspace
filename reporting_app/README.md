# Sales & Customer Reporting Pipeline

A batch pipeline that reads sales/customer CSVs, loads them into an indexed
SQLite database, computes analyses with pandas, generates matplotlib
charts, and renders a single self-contained HTML report.

> **Status:** Project structure and module contracts are scaffolded.
> Function bodies are intentionally left as `raise NotImplementedError`
> stubs pending the next implementation step.

## Project Structure

```
reporting_app/
├── config/
│   └── config.yaml            # paths, chunk size, DB PRAGMAs, thresholds
├── data/
│   ├── sales_data-2.csv
│   └── customers_data.csv
├── db/
│   └── reporting.db           # generated at runtime
├── src/
│   ├── config.py               # YAML config loader + path resolution
│   ├── ingestion.py             # chunked CSV readers (dtype-safe)
│   ├── validation.py            # clean/reject splitting, data-quality checks
│   ├── db_loader.py              # schema DDL, indexes, bulk inserts
│   ├── analysis.py               # pandas aggregations over SQLite
│   ├── visualization.py          # matplotlib chart generation
│   ├── report_builder.py         # Jinja2 HTML report assembly
│   └── utils/
│       ├── logging_config.py     # centralized rotating logger
│       └── db_utils.py            # SQLite connection + PRAGMA management
├── templates/
│   └── report_template.html      # Jinja2 template + inline CSS
├── output/
│   ├── charts/                   # generated PNGs per run
│   ├── reports/                  # generated HTML reports
│   └── rejected/                 # quarantined bad rows
├── logs/                          # rotating pipeline logs
├── tests/                         # unit tests per module
├── main.py                        # CLI entry point / orchestrator
└── requirements.txt
```

## Module Responsibilities (separation of concerns)

| Module | Owns | Does NOT own |
|---|---|---|
| `src/config.py` | Config parsing, path resolution | Logging, DB, business rules |
| `src/utils/logging_config.py` | Logger setup (file + console) | Config parsing, pipeline logic |
| `src/utils/db_utils.py` | SQLite connections, PRAGMAs | Schema DDL, business SQL |
| `src/ingestion.py` | Chunked CSV reading, dtypes | Validation, DB writes |
| `src/validation.py` | Clean/reject splitting, DQ checks | CSV reading, DB writes |
| `src/db_loader.py` | Schema DDL, indexes, bulk inserts | Validation rules, analysis SQL |
| `src/analysis.py` | Read-only aggregation queries | DDL/inserts, charts, HTML |
| `src/visualization.py` | Chart image generation | Aggregation, HTML |
| `src/report_builder.py` | HTML assembly from pre-built inputs | Aggregation, chart generation |
| `main.py` | Stage sequencing, CLI, exit codes | Any business/analysis logic |

## Data Notes

- `sales_data-2.csv`: 2,500 rows — `Transaction_ID, Date, Customer_ID,
  Product_Category, Product_Name, Quantity, Unit_Price, Total_Amount,
  Payment_Method`.
- `customers_data.csv`: 1,000 rows — `Customer_ID, Name, Age, Gender,
  Location, Total_Spent`.
- 920 of the sales file's unique `Customer_ID`s match the customers table
  (0 unmatched sales rows as of the last validation pass), so joined
  customer-insight analysis is meaningful.

## Next Step

Implement the function bodies in dependency order: `config.py` →
`utils/logging_config.py` / `utils/db_utils.py` → `ingestion.py` →
`validation.py` → `db_loader.py` → `analysis.py` → `visualization.py` →
`report_builder.py` → `main.py`, then run `python main.py` end-to-end and
verify the generated report under `output/reports/`.
