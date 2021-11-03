from view.window.controller import MainWindow
from view.window.controller.Widgets.LoginWidget import LoginWidget
from . import appConstants


def start():
    """
    Starts the Application. Does the prior setup.
    Then starts the login sequence into the camera...
    When successful will show other windows
    """
    appConstants.MAIN_WINDOW = MainWindow()
    root = appConstants.MAIN_WINDOW.window
    # Start with login
    appConstants.LOGIN_WIDGET = LoginWidget(root)
    root.mainloop()
