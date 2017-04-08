#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-

# Copyright (C) 2017 Denis Ollier
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

"""
Python implementation of the rpmatch(3) libc function.

Usage example in python scripts:

    from rpmatch import rpmatch

    response = raw_input("Do you agree? ")

    if rpmatch(response) == 1:
        # User agreed
        ...
    else:
        # User did not agree
        ...
"""

__all__ = ['rpmatch']
__author__ = 'Denis Ollier'
__copyright__ = 'Copyright (C) 2017 Denis Ollier'
__license__ = 'GPL-3.0-or-later'
__version__ = '1.0.0'

import locale
import re


def rpmatch(response):
    """
    Determine if the answer to a question is affirmative or negative

    Returns:
      0 for a recognized negative response,
      1 for a recognized affirmative response,
      -1 for an unrecognized response
    """

    # locale.nl_langinfo is not supported for all OSes (e.g: windows)
    try:
        yes = locale.nl_langinfo(locale.YESEXPR)
        no = locale.nl_langinfo(locale.NOEXPR)
    except AttributeError:
        yes = "^[yY]"
        no = "^[nN]"

    if re.match(yes, response):
        result = 1
    elif re.match(no, response):
        result = 0
    else:
        result = -1

    return result

# vi: set ft=python et sw=4 ts=4:
