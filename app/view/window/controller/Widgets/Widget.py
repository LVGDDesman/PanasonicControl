class Widget:
    """
    Widgets represent tkinter frames which can be added to a window.
    """

    def __init__(self):
        self._widget = None

    @property
    def widget(self):
        return self._widget
