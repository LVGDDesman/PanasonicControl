#!/usr/bin/env python3

class Command():
    """
    Inheritance Class for all executable commands
    """
    def __init__(self):
        self = self

    @staticmethod
    def execute(*args) -> bool:
        """
        execute-function, that should be implemented by every Child class.
        """
        return False
