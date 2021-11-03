from tkinter import *

from model.design_pattern import Singleton
from .Window import Window


class MainWindow(Window, metaclass=Singleton):
    """
    Main window of the application. All the stuff that will be visualized in the app will have this window as root.
    """
    _APPLICATION_NAME = "Panasonic WLAN Control"
    _VERSION = "0.0.1"
    _CURRENT_WINDOW_NAME = ""
    _WIDTH = 1920
    _HEIGHT = 1080

    def __init__(self):
        super().__init__(self._CURRENT_WINDOW_NAME, self._WIDTH, self._HEIGHT)
        self._window = None

    @property
    def window(self):
        # If we already have created a main window return that
        if self._window is not None:
            return self._window
        # Create main top level window
        self._window = Tk()
        self._window.title(self._APPLICATION_NAME + " " + self._VERSION)
        self._window.geometry(str(self._WIDTH) + "x" + str(self._HEIGHT))
        self._window.minsize(self._min_width, self._min_height)
        return self._window
