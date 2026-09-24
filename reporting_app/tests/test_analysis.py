"""Tests for src.analysis.

1. RESPONSIBILITY
    Verify each analysis function produces correctly shaped/valued
    DataFrames against a small, known SQLite fixture database (seeded with
    a handful of hand-crafted sales/customers rows with predictable
    aggregation results).

2. DEPENDENCIES
    - ``pytest``
    - ``sqlite3`` (stdlib)
    - ``pandas``
    - ``src.analysis`` (module under test)
    - ``src.db_loader`` (to seed the fixture database schema/rows)

3. INPUT / OUTPUT
    Input: an in-memory SQLite database seeded with known rows.
    Output: assertions on computed KPI values, category totals, top-N
    ordering, and customer-insight joins.

4. FUNCTIONS (planned test cases, not yet implemented)
    - ``test_compute_kpis_matches_expected_totals``
    - ``test_compute_time_trend_groups_by_day``
    - ``test_compute_category_performance_sums_correctly``
    - ``test_compute_top_products_orders_by_revenue_desc``
    - ``test_compute_payment_method_mix_sums_to_total``
    - ``test_compute_customer_insights_handles_unmatched_customers``
    - ``test_run_all_analyses_returns_all_expected_keys``

5. WHAT IT SHOULD NOT CONTAIN
    - No use of the real project database or production CSVs.
    - No matplotlib/Jinja2 dependencies — analysis tests check DataFrame
      values only.
"""
