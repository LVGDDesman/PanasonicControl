from tkinter import Frame, SUNKEN, Label, LEFT, RIGHT, TOP, X

from model.design_pattern.Singleton import Singleton
from view.window.controller.Widgets.Widget import Widget


class StatusBarWidget(Widget, metaclass=Singleton):
    """
    Widget that displays information about the status of the camera and the app.
    """

    def __init__(self, root):
        """
        Build new statusBarWidget and adds it to the root window

        :param root: Window widget will be attached to
        """
        super().__init__()
        self._widget = self._create_status_bar(root)

    def _create_status_bar(self, root):
        """
        Creates a status bar at the top of the window

        :param root: Window widget will be attached to
        :return: This widget
        """
        # Status bar frame
        status_bar = Frame(root, bd=1, relief=SUNKEN)
        # Camera name
        camera_model = Label(status_bar, text="G81 DMC")
        camera_model.pack(side=LEFT, pady=10)
        # Current mode
        execution_mode = Label(status_bar, text="EXECUTING")
        execution_mode.place(relx=.5, rely=.5, anchor="center")
        # Camera status
        status = Label(status_bar, text="disconnected")
        status.pack(side=RIGHT, pady=10)
        # Finishing it
        status_bar.pack(side=TOP, fill=X)

        return status_bar
