import os.path

from interfac.create_gui import GuiCreator
import configparser


def run_app():
    gui = GuiCreator()
    gui.create_main_gui()


if __name__ == "__main__":
    run_app()


