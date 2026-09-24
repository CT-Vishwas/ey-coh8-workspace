"""Chunked CSV ingestion for the sales and customer datasets.

1. RESPONSIBILITY
    Read the raw ``sales_data-2.csv`` and ``customers_data.csv`` files from
    disk in bounded-memory chunks, with explicit dtypes and date parsing, so
    the pipeline can scale to files far larger than what fits comfortably in
    memory. This module ONLY reads and yields raw chunks — it does not
    validate business rules or write to the database.

2. DEPENDENCIES
    - ``pandas`` for ``read_csv`` with ``chunksize``.
    - ``src.utils.logging_config.get_logger`` for progress logging (rows
      read per chunk).
    - No dependency on ``validation.py`` or ``db_loader.py`` — this module
      sits upstream of both and knows nothing about them.

3. INPUT / OUTPUT
    Input:
        - File paths to the sales and customers CSVs (from config).
        - Chunk size (int, from config).
    Output:
        - Generators yielding raw ``pandas.DataFrame`` chunks, one per CSV,
          with columns cast to the expected dtypes and the ``Date`` column
          parsed to ``datetime64`` for the sales file.
        - No disk writes; purely a read/yield module.

4. FUNCTIONS
    - ``read_sales_chunks(csv_path: str, chunksize: int) -> Iterator[pd.DataFrame]``
        Yields raw sales DataFrame chunks with dtype map applied
        (``Transaction_ID``, ``Customer_ID``, ``Product_Category``,
        ``Product_Name``, ``Payment_Method`` as string; ``Quantity`` as
        int; ``Unit_Price``/``Total_Amount`` as float; ``Date`` parsed as
        datetime).
    - ``read_customers_chunks(csv_path: str, chunksize: int) -> Iterator[pd.DataFrame]``
        Yields raw customer DataFrame chunks with dtype map applied
        (``Customer_ID``, ``Name``, ``Gender``, ``Location`` as string;
        ``Age`` as int; ``Total_Spent`` as float).
    - ``get_sales_dtype_map() -> dict``
        Returns the canonical dtype mapping for the sales CSV (single
        source of truth, reused by validation/tests).
    - ``get_customers_dtype_map() -> dict``
        Returns the canonical dtype mapping for the customers CSV.

5. WHAT IT SHOULD NOT CONTAIN
    - No validation/quarantine logic (null checks, duplicate checks, domain
      checks) — that belongs entirely in ``validation.py``.
    - No SQLite writes — that belongs in ``db_loader.py``.
    - No matplotlib/Jinja2 imports — this module is I/O-in only.
    - No silent dtype coercion failures swallowed here; if ``read_csv``
      raises on malformed data, let it propagate (or catch narrowly and
      re-raise with context) rather than returning partial/guessed data.
"""
from __future__ import annotations

from typing import Any, Dict, Iterator

import pandas as pd


def get_sales_dtype_map() -> Dict[str, Any]:
    """Return the canonical dtype mapping for the sales CSV columns.

    Not yet implemented.
    """
    raise NotImplementedError


def get_customers_dtype_map() -> Dict[str, Any]:
    """Return the canonical dtype mapping for the customers CSV columns.

    Not yet implemented.
    """
    raise NotImplementedError


def read_sales_chunks(csv_path: str, chunksize: int) -> Iterator[pd.DataFrame]:
    """Yield raw sales DataFrame chunks from the CSV at ``csv_path``.

    Not yet implemented.
    """
    raise NotImplementedError


def read_customers_chunks(csv_path: str, chunksize: int) -> Iterator[pd.DataFrame]:
    """Yield raw customer DataFrame chunks from the CSV at ``csv_path``.

    Not yet implemented.
    """
    raise NotImplementedError
