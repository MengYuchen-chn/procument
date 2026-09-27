# Python 3.14.7 Workspace Template

This workspace uses `pyenv` with Python `3.14.7` and a local `.venv`.

## Quick Start

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
```

## Project Layout

```text
/workspace
|-- .python-version
|-- pyproject.toml
|-- src/workspace_app/
|-- tests/
`-- .vscode/settings.json
```
