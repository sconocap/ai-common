import os

from ai_common.file_operations.paths import (
    get_absolute_path,
    get_package_path,
    get_project_path,
)


def test_get_package_path():
    # get_package_path should return the directory of the calling script (this test file)
    expected_path = os.path.dirname(os.path.abspath(__file__))
    assert get_package_path() == expected_path


def test_get_absolute_path():
    # get_absolute_path should build paths relative to the calling script's directory
    test_dir = os.path.dirname(os.path.abspath(__file__))
    expected_path = os.path.join(test_dir, "test_paths.py")
    assert get_absolute_path("test_paths.py") == expected_path


def test_get_project_path():
    # get_project_path should find project root (where pyproject.toml is) and build paths relative to it
    # The project root is ai-common/ (parent of test/ directory)
    project_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    # Test finding pyproject.toml
    pyproject_path = get_project_path("pyproject.toml", start_file=__file__)
    assert pyproject_path == os.path.join(project_root, "pyproject.toml")
    assert os.path.isfile(pyproject_path)

    # Test building a path to src directory
    src_path = get_project_path("src/ai_common/__init__.py", start_file=__file__)
    expected_src_path = os.path.join(project_root, "src", "ai_common", "__init__.py")
    assert src_path == expected_src_path
