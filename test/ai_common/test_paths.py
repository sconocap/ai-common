import os

from ai_common.file_operations.paths import get_absolute_path, get_package_path


def test_get_package_path():
    # get_package_path should return the directory of the calling script (this test file)
    expected_path = os.path.dirname(os.path.abspath(__file__))
    assert get_package_path() == expected_path


def test_get_absolute_path():
    # get_absolute_path should build paths relative to the calling script's directory
    test_dir = os.path.dirname(os.path.abspath(__file__))
    expected_path = os.path.join(test_dir, "test_paths.py")
    assert get_absolute_path("test_paths.py") == expected_path
Summarizing the problem:


[3 tools called]


## Problem Summary

**Two different execution contexts with conflicting import requirements:**

### Context 1: Script execution
- Command: `uv run src/intropyproject_classify_pet_images/data/check_images.py`
- Python runs the script directly (not as a package)
- `check_images.py` uses: `from classify_images import classify_images` (simple import)
- `classify_images.py` needs to import `classifier`
- Works with: `from classifier import classifier` (simple import, same directory)

### Context 2: Test execution
- Command: `uv run task test` (runs pytest)
- Pytest imports modules as a package: `from src.intropyproject_classify_pet_images.data.classify_images import classify_images`
- `classify_images.py` is imported as part of a package
- Needs: `from src.intropyproject_classify_pet_images.data.classifier import classifier` (absolute package import)
- Fails with: `from classifier import classifier` (not a top-level module)

### The conflict
- Script execution expects simple imports (`from classifier import classifier`)
- Test execution expects package imports (`from src.intropyproject_classify_pet_images.data.classifier import classifier`)
- The same file must work in both contexts

### Current state
- Using try/except as a workaround (not ideal)
- Pytest configured with `pythonpath = ["."]` in `pyproject.toml`

### Standard solutions
1. Use relative imports (`from .classifier import classifier`) and run scripts as modules
2. Standardize on absolute package imports and adjust script execution
3. Add `__init__.py` files and use proper package structure

Which approach should we take?