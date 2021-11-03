from view.window import appConstants
from view.window.controller.Widgets.StatusBarWidget import StatusBarWidget


def _show_exec_view():
    """
    Shows the execution view to the user.
    This shall be the main window of the application.
    The user will see info of the camera and the status.
    The user will be able to execute single commands and see their results.
    """
    root = appConstants.MAIN_WINDOW.window
    appConstants.STATUS_BAR_WIDGET = StatusBarWidget(root)
    appConstants.LOGIN_WIDGET.widget.destroy()
