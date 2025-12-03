# File Operations

The `file_operations.paths` module provides utilities for working with file paths.

## Path Operations

### `get_package_path()`

Returns the directory path of the script that calls this function. This is useful for getting the directory where the calling script is located, rather than the directory of this utility module.

```python
from ai_common.file_operations.paths import get_package_path

# Get the directory where the calling script is located
script_dir = get_package_path()
```

### `get_absolute_path(relative_path: str)`

Builds an absolute path to a file located in the same directory as the calling script. This is useful for accessing data files that live alongside the script that calls this function.

```python
from ai_common.file_operations.paths import get_absolute_path

# Get absolute path to a file in the same directory as the calling script
data_file = get_absolute_path("data.txt")
```

### `get_project_path(relative_path: str, start_file: str | None = None)`

Builds an absolute path to a file relative to the project root. Finds the project root by looking for `pyproject.toml` starting from the directory of `start_file` (or the calling script) and walking up the directory tree.

This is useful for test files or scripts that need to access files in the project structure (e.g., data files in `src/`).

```python
from ai_common.file_operations.paths import get_project_path

# In tests/test_something.py
data_file = get_project_path("src/package/data/file.txt")
# Returns: /path/to/project/src/package/data/file.txt

# Or specify a starting file explicitly
data_file = get_project_path("src/package/data/file.txt", start_file=__file__)
```

