from tkinter import Frame, Label, LEFT, Button

from view.window.controller import MainWindow
from view.window.controller.Widgets.Widget import Widget
from view.window.controller.WindowControlls import _show_exec_view
from view.utils.table import create_table
from model.design_pattern.Singleton import Singleton


class LoginWidget(Widget, metaclass=Singleton):
    """
    Widget that allows login into the camera. The user is demanded to fill the credentials to proceed
    """

    def __init__(self, root):
        """
        Build new loginWidget and adds it to the root window

        :param root: Window widget will be attached to
        """
        super().__init__()
        self._widget = _create_login_widget(root)


def _create_login_widget(root):
    """
    Creates a login screen filling the window

    :param root: Window widget will be attached to
    :return: This widget
    """
    main_window = MainWindow()
    login_frame = Frame(root, width=main_window.width, height=main_window.height)

    login_text = "Login to Camera"
    login_label = Label(login_frame, text=login_text, justify=LEFT)
    login_label.pack()

    information_label = Label(login_frame)
    information = [("IP-adress", "XX.XX.XX.XX"), ("Client-Name", "XXXXX")]

    create_table(information_label, information)
    information_label.pack()

    login_label1 = Label(login_frame, text="Make sure to connect to the camera network first!", fg="red")
    login_label1.pack()

    login_button = Button(login_frame, text="Login", command=_show_exec_view)
    login_button.pack()

    login_frame.place(in_=root, anchor="c", relx=.5, rely=.5)

    return login_frame
