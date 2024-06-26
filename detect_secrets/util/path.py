import os
from pathlib import Path
from typing import Optional


def get_relative_path(root: str, path: str) -> Optional[str]:
    if Path(os.getcwd()) == Path(root):
        return get_relative_path_if_in_cwd(path)

    return os.path.realpath(path)[len(root + '/'):]


def get_relative_path_if_in_cwd(path: str) -> Optional[str]:
    filepath = os.path.realpath(path)[len(os.getcwd() + '/'):]
    if os.path.isfile(filepath):
        return filepath

    return None


def convert_local_os_path(path: str) -> str:
    # Linux filesystem, replace \\ with /
    if os.sep == '/':
        path = path.replace('\\', '/')
        return path
    else:
        path = path.replace('/', '\\')
        return path
