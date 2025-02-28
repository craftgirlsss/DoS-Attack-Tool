#!/usr/bin/env python
from src.argument_handler import ArgumentHandler
from src.banner import Header
from src.helpers import Helpers

if __name__ == "__main__":
    Helpers.clear_terminal()
    Header()
    ArgumentHandler()