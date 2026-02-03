import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None

executables = [
    Executable("main.py", base=base, target_name="bjj-system.exe", icon="./views/icons/window_icon.ico"),
]

packages = [
    "PySide6.QtCore",
    "PySide6.QtGui",
    "PySide6.QtWidgets",
    "PySide6.QtNetwork",
    "shiboken6",
    "requests",
    "pkg_resources",
    "multiprocessing",
    "idna",
    "alembic",
    "sqlalchemy",
    "sqlalchemy.dialects.sqlite",
    "logging",
    "asyncio",
    "random",
    "sys",
    "threading"
]

include_files = [
    ('views/icons', 'views/icons'),
    ('alembic', 'alembic'),
    ('alembic.ini', 'alembic.ini')
]

build_exe_options = {
    "packages": packages,
    "include_files": include_files,
    "includes": [
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
    ],
    "excludes": ["tkinter", "unittest", "email", "http", "xml", "pydoc"],
    "zip_include_packages": ["*"],
    "zip_exclude_packages": ["PySide6", "shiboken6"],
    "optimize": 0,
    "include_msvcr": True
}

setup(
    name="BJJ Admin",
    version="1.0",
    description="Sistema de gerenciamento de academias de jiu-jitsu",
    options={"build_exe": build_exe_options},
    executables=executables,
)