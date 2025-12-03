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
