class Window:
    """
    Base Class for any window in the application
    """

    def __init__(self, current_window_name, width, height,
                 min_width=400, min_height=300):
        self._current_window_name = current_window_name
        self._width = width
        self._height = height
        self._min_width = min_width
        self._min_height = min_height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
