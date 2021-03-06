"""
Module to save the many types of constants used by the app. Mostly containing paths to static picture files.
"""

from pathlib import Path

PATH_TO_ICON: str = str(Path(__file__).parent.parent) + "/resources/icon.png"
""" Path to the standard icon of the application """

MAIN_WINDOW: "MainWindow" = None
"""
The main window
"""
LOGIN_WIDGET: "LoginWidget" = None
""" The login widget"""

STATUS_BAR_WIDGET: "StatusBarWidget" = None
""" The status bar widget"""
