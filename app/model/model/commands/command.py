#!/usr/bin/env python3
"""
Inheritance Class for all executable commands
"""

class Command():
    
    def __init__(self):
        self = self

    @staticmethod
    def execute(*args) -> bool:
        return False
