"""Tests for src.ingestion.

1. RESPONSIBILITY
    Verify that chunked CSV reading produces correctly typed DataFrame
    chunks of the expected shape for both the sales and customers files,
    using small in-memory/temp-file fixtures (not the full production CSVs).

2. DEPENDENCIES
    - ``pytest``
    - ``pandas``
    - ``src.ingestion`` (module under test)

3. INPUT / OUTPUT
    Input: small synthetic CSV fixtures written to a pytest ``tmp_path``.
    Output: assertions only; no files persisted beyond the test's tmp dir.

4. FUNCTIONS (planned test cases, not yet implemented)
    - ``test_read_sales_chunks_returns_expected_dtypes``
    - ``test_read_sales_chunks_respects_chunksize``
    - ``test_read_customers_chunks_returns_expected_dtypes``
    - ``test_get_sales_dtype_map_contains_all_columns``
    - ``test_get_customers_dtype_map_contains_all_columns``

5. WHAT IT SHOULD NOT CONTAIN
    - No assertions against the real data/*.csv files (use small fixtures
      so tests run fast and deterministically).
    - No SQLite/db_loader dependencies — ingestion tests are isolated to
      CSV reading only.
"""
