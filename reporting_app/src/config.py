"""Configuration loader for the reporting pipeline.

1. RESPONSIBILITY
    Load ``config/config.yaml`` and resolve every entry under ``paths`` to an
    absolute filesystem path (relative to the project root), so every other
    module can rely on ready-to-use, unambiguous paths regardless of the
    process's current working directory. This is the ONLY module that knows
    where the project root is and how config values map to paths.

2. DEPENDENCIES
    - PyYAML (``yaml``) for parsing the config file.
    - ``pathlib.Path`` (stdlib) for path resolution.
    - No dependency on any other ``src`` module (this sits at the bottom of
      the dependency graph; everything else depends on it, not vice versa).

3. INPUT / OUTPUT
    Input:
        - Path to a YAML config file (defaults to ``config/config.yaml`` at
          the project root).
    Output:
        - A plain ``dict`` representing the parsed config, with the
          ``paths`` sub-dict rewritten to absolute path strings. No I/O side
          effects beyond reading the YAML file.

4. FUNCTIONS
    - ``load_config(config_path: Path | str = DEFAULT_CONFIG_PATH) -> dict``
        Reads and parses the YAML file, resolves ``paths`` entries to
        absolute paths, and returns the resulting config dict.
    - (module-level constants) ``PROJECT_ROOT``, ``DEFAULT_CONFIG_PATH``
        Computed once at import time from this file's location.

5. WHAT IT SHOULD NOT CONTAIN
    - No logging setup (that belongs in ``utils/logging_config.py``).
    - No directory creation side effects (e.g. ``mkdir``) — that is the
      responsibility of the modules that actually write to those
      directories (ingestion, db_loader, visualization, report_builder).
    - No business logic, validation rules, or SQL — this module only
      resolves configuration, it does not interpret it.
    - No caching/singleton state beyond simple re-parsing; if repeated
      re-reads become a performance issue, memoization can be added later
      without changing the public contract.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"


def load_config(config_path: Path | str = DEFAULT_CONFIG_PATH) -> Dict[str, Any]:
    """Load the YAML config and resolve all ``paths`` entries to absolute paths.

    Not yet implemented.
    """
    raise NotImplementedError
