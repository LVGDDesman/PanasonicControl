from view.window.controller.tkinter_test import Registration_window


def start():
    """
    Starts the Application. Does the prior setup.
    Then starts the login sequence into the camera...
    When successful will show other windows
    """

    show_exec_view()
    a = Registration_window(1920, 1080)
    a.initialize_login()


def show_exec_view():
    """
    Shows the execution view to the user.
    This shall be the main window of the application.
    The user will see info of the camera and the status.
    The user will be able to execute single commands and see their results.
    """

