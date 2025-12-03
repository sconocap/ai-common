import inspect
import os


def get_package_path() -> str:
    """
    Returns the directory path of the script that calls this function.

    This is useful for getting the directory where the calling script is located,
    rather than the directory of this utility module.
    """
    # Get the current frame and walk up the stack to find the actual caller
    # (skipping frames from this module)
    current_file = os.path.abspath(__file__)
    frame = inspect.currentframe()
    try:
        # Walk up the stack, skipping frames from this module
        caller_frame = frame.f_back
        while caller_frame is not None:
            caller_file = caller_frame.f_globals.get("__file__")
            if caller_file is None:
                # No __file__ in this frame, try next one
                caller_frame = caller_frame.f_back
                continue
            caller_file_abs = os.path.abspath(caller_file)
            # If this frame is from a different file, we found our caller
            if caller_file_abs != current_file:
                return os.path.dirname(caller_file_abs)
            # Otherwise, continue up the stack
            caller_frame = caller_frame.f_back

        # Fallback to __file__ if no external caller found
        return os.path.dirname(os.path.abspath(__file__))
    finally:
        del frame  # Avoid reference cycles


def get_absolute_path(relative_path: str) -> str:
    """
    Build an absolute path to a file located in the same directory
    as the calling script.

    This is useful for accessing data files that live alongside the
    script that calls this function.
    """
    package_dir = get_package_path()
    return os.path.join(package_dir, relative_path)


def get_project_path(relative_path: str, start_file: str | None = None) -> str:
    """
    Build an absolute path to a file relative to the project root.

    Finds the project root by looking for `pyproject.toml` starting from
    the directory of `start_file` (or the calling script) and walking up
    the directory tree.

    This is useful for test files or scripts that need to access files
    in the project structure (e.g., data files in `src/`).

    Args:
        relative_path: Path relative to project root (e.g., "src/package/data/file.txt")
        start_file: Optional file path to start searching from. If None, uses the
                   calling script's location (via `__file__`).

    Returns:
        Absolute path to the file.

    Example:
        ```python
        # In tests/test_something.py
        from ai_common.file_operations import get_project_path

        data_file = get_project_path("src/package/data/file.txt")
        # Returns: /path/to/project/src/package/data/file.txt
        ```
    """
    if start_file is None:
        # Get the calling script's directory
        start_dir = get_package_path()
    else:
        start_dir = os.path.dirname(os.path.abspath(start_file))

    # Walk up the directory tree to find project root (marked by pyproject.toml)
    current_dir = start_dir
    while current_dir != os.path.dirname(current_dir):  # Stop at filesystem root
        pyproject_path = os.path.join(current_dir, "pyproject.toml")
        if os.path.isfile(pyproject_path):
            # Found project root
            return os.path.join(current_dir, relative_path)
        current_dir = os.path.dirname(current_dir)

    # If pyproject.toml not found, assume start_dir's parent is project root
    # (common case: tests/ -> project root)
    project_root = os.path.dirname(start_dir)
    return os.path.join(project_root, relative_path)
