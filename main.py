import shiboken6

import os
import sys

from PySide6.QtWidgets import QApplication

from alembic import command
from alembic.config import Config
from tendo.singleton import SingleInstanceException
from tendo import singleton

from engine import Session
from models import Plan, LessonClass
from views.main_view import MainView


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.abspath("."), relative)

def run_migrations():
    config = Config(resource_path("alembic.ini"))
    command.upgrade(config, "head")

def ensure_defaults(session):
    if not session.get(Plan, 1):
        session.add(
            Plan(
                id=1,
                name="Padrão",
                value="0",
                observation="Plano padrão"
            )
        )

    if not session.get(LessonClass, 1):
        session.add(
            LessonClass(
                id=1,
                name="Padrão",
                observation="Turma padrão"
            )
        )

    session.commit()



if __name__ == "__main__":
    is_running = False

    try:
        me = singleton.SingleInstance()
    except SingleInstanceException as e:
        is_running = True

    if not is_running:
        run_migrations()

        app = QApplication(sys.argv)
        app.setStyle("windowsvista")

        ensure_defaults(Session())

        main_view = MainView()
        main_view.show()
        sys.exit(app.exec())

