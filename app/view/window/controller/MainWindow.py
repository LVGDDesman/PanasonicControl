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

    def create_window(self):
        root = Tk()
        root.title(self._APPLICATION_NAME + " " + self._VERSION)
        root.geometry(str(self._WIDTH) + "x" + str(self._HEIGHT))
        root.minsize(self._min_width, self._min_height)
        return root

    def create_status_bar(self, root):
        status_bar = Frame(root, bd=1, relief=SUNKEN)
        
        camera_model = Label(status_bar, text="G81 DMC")
        camera_model.pack(side=LEFT, pady=10)
        
        
        execution_mode = Label(status_bar, text="EXECUTING")
        execution_mode.place(relx=.5, rely=.5, anchor="center")

        status = Label(status_bar, text="disconnected")
        status.pack(side=RIGHT, pady=10)

        status_bar.pack(side=TOP, fill=X)
        
        return
