import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None

executables = [
    Executable("main.py", base=base, target_name="bjj-system.exe", icon="C:\\Users\\vitor\\workspace\\jitjitsu-system\\views\\icons\\window_icon.ico"),
]

packages = [
    "PySide6", "requests", "pkg_resources", "multiprocessing", "idna", "alembic",
    "sqlalchemy", "logging", "asyncio", "random", "sys", "threading"
]

include_files = [
    ('views/icons', 'views/icons'),
    ('views/ui', 'views/ui'),
    ('alembic', 'alembic'),
    ('alembic.ini', 'alembic.ini'),
    ('utils', 'utils')
]

build_exe_options = {
    "packages": packages,
    "include_files": include_files,
    "excludes": [],
}

setup(
    name="BJJ Admin",
    version="0.0",
    description="",
    options={"build_exe": build_exe_options},
    executables=executables,
)