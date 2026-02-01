# AGENTS.md — netmiko_tool

## Commands
- Run tool: `python network_tool.py`
- Run with args: `python network_tool.py --commands "show version" --format json`
- Lint: `python -m py_compile network_tool.py`
- Format (recommended): `black network_tool.py`
- Tests: none yet (add `pytest` when introducing tests)
- Single test (future): `pytest tests/test_network_tool.py::test_name`

## Code Style
- Language: Python 3.10+
- Formatting: Black defaults; 88‑char lines
- Imports: stdlib → third‑party → local; no duplicates
- Types: use type hints for all functions
- Naming: `snake_case` for functions/vars, `UPPER_CASE` for constants
- Errors: catch specific exceptions, log stack traces, never swallow silently
- Logging: use `logging`, no `print` in library code
- Secrets: never hardcode credentials; use env vars
- I/O: functions return data; CLI handles printing

## Notes
- This is a learning repo; prioritize clarity over cleverness
- No Cursor or Copilot rules detected