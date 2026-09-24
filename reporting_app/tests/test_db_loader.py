"""Tests for src.db_loader.

1. RESPONSIBILITY
    Verify schema creation is idempotent, indexes are created successfully
    after load, bulk-load functions insert the expected row counts, and
    audit/data-quality rows are recorded correctly — all against a
    temporary, disposable SQLite database (never the real db/reporting.db).

2. DEPENDENCIES
    - ``pytest``
    - ``sqlite3`` (stdlib)
    - ``pandas``
    - ``src.db_loader`` (module under test)
    - ``src.utils.db_utils.get_connection``

3. INPUT / OUTPUT
    Input: an in-memory (``:memory:``) or ``tmp_path``-based SQLite
    database, small synthetic clean DataFrames.
    Output: assertions on row counts, index existence
    (``sqlite_master`` queries), and audit table contents.

4. FUNCTIONS (planned test cases, not yet implemented)
    - ``test_create_schema_is_idempotent``
    - ``test_create_indexes_creates_expected_indexes``
    - ``test_load_sales_chunk_inserts_expected_row_count``
    - ``test_load_customers_chunk_inserts_expected_row_count``
    - ``test_record_load_audit_persists_row``
    - ``test_record_data_quality_persists_summary``

5. WHAT IT SHOULD NOT CONTAIN
    - No use of the real project database file.
    - No CSV reading — DataFrames are constructed directly in the test.
"""
