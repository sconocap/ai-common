# ai-common

Shared utilities for the masters_in_ai workspace (paths, file operations, etc.).

## Overview

`ai-common` provides common utility functions for path and file operations that are used across projects in the masters_in_ai workspace. It simplifies working with file paths relative to calling scripts or project roots.

## Installation

This package requires Python >=3.14.

### Development Setup

```bash
# Install dependencies
uv sync

# Or install with dev dependencies
uv sync --dev
```

## Usage

### File Operations

For detailed documentation on file operations and path utilities, see the [file_operations README](src/ai_common/file_operations/README.md).

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Or use the task runner
uv run task test
```

### Code Quality

The project uses several tools for code quality:

- **Ruff**: Linting and formatting
- **MyPy**: Type checking
- **Pytest**: Testing

Available tasks:

```bash
# Lint code
uv run task lint

# Format code
uv run task format

# Type check
uv run task typecheck

# Run all checks (lint, format, typecheck, test)
uv run task check
```

## Project Structure

```
ai-common/
├── src/
│   └── ai_common/
│       ├── __init__.py
│       └── file_operations/
│           ├── __init__.py
│           ├── paths.py
│           └── README.md
├── test/
│   └── ai_common/
│       └── test_paths.py
├── pyproject.toml
└── README.md
```

## License

[Add license information here]

## Author

Nico

