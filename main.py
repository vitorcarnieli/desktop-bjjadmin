import sys

from PySide6.QtWidgets import QApplication

from alembic import command
from alembic.config import Config
from tendo.singleton import SingleInstanceException
from tendo import singleton

from views.main_view import MainView


def run_migrations():
    """Execute migrations."""
    config = Config("alembic.ini")
    upgrade_revision = "head"
    command.upgrade(config, upgrade_revision)


if __name__ == "__main__":
    is_running = False

    try:
        me = singleton.SingleInstance()
    except SingleInstanceException as e:
        is_running = True

    if not is_running:
        run_migrations()

        app = QApplication(sys.argv)

        main_view = MainView()
        main_view.show()
        sys.exit(app.exec())

