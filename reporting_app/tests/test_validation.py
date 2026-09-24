"""Tests for src.validation.

1. RESPONSIBILITY
    Verify that ``validate_sales_chunk`` and ``validate_customers_chunk``
    correctly split rows into clean vs. rejected based on each rule (nulls,
    duplicates, domain checks, amount-tolerance mismatch, unmatched
    customer references), and that ``summarize_data_quality`` produces
    correct issue-type counts.

2. DEPENDENCIES
    - ``pytest``
    - ``pandas``
    - ``src.validation`` (module under test)

3. INPUT / OUTPUT
    Input: small synthetic DataFrames covering each validation rule (one
    row that should pass, one row per rejection reason).
    Output: assertions on the returned (clean, rejected) DataFrames and the
    ``reject_reason`` values.

4. FUNCTIONS (planned test cases, not yet implemented)
    - ``test_validate_sales_chunk_accepts_clean_rows``
    - ``test_validate_sales_chunk_rejects_negative_quantity``
    - ``test_validate_sales_chunk_rejects_amount_mismatch``
    - ``test_validate_sales_chunk_flags_unmatched_customer_id``
    - ``test_validate_customers_chunk_rejects_duplicate_customer_id``
    - ``test_summarize_data_quality_counts_by_issue_type``

5. WHAT IT SHOULD NOT CONTAIN
    - No SQLite access — validation is pure pandas logic.
    - No dependency on the real production CSVs.
"""
