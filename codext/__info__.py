# -*- coding: UTF-8 -*-
"""Codext package information.

"""
import os

__author__    = "Alexandre D'Hondt"
__copyright__ = "© 2019 A. D'Hondt"
__email__     = "alexandre.dhondt@gmail.com"
__license__   = "AGPLv3 (http://www.gnu.org/licenses/agpl.html)"
__source__    = "https://github.com/dhondta/python-codext"

with open(os.path.join(os.path.dirname(__file__), "VERSION.txt")) as f:
    __version__ = f.read().strip()
