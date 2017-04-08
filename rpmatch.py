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

It can be imported and used in python scripts or directly run as a script.

Usage example in python scripts:

    from rpmatch import rpmatch

    response = raw_input("Do you agree? ")

    if rpmatch(response) == 1:
        # User agreed
        ...
    else:
        # User did not agree
        ...

Usage as a script from command line:

    > python -m rpmatch response

When used as a script, the following exit status codes are used:
  - 0 for a recognized affirmative response
  - 1 for a recognized negative response
  - 2 for an unrecognized response
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


# Make module runnable as a script
if __name__ == "__main__":

    import optparse  # argparse is better but not included in python 2.6 stdlib
    import os
    import sys

    def process_command_line():
        """Process program command line arguments"""

        # Setup option parser
        usage = (
          "\n  %prog response"
          "\n  %prog option"
        )

        description = (
          "Determine if the answer to a question is affirmative or negative"
        )

        optparser = optparse.OptionParser(usage=usage, description=description)

        # Register options
        optparser.add_option(
          "-V", "--version",
          action="store_true",
          help="show version information and exit"
        )

        # Convert arguments to local variables
        (keyword_args, positional_args) = optparser.parse_args()

        # Handle keyword arguments
        if keyword_args.version:
            sys.stdout.write(
              "%s %s\n" % (os.path.basename(sys.argv[0]), __version__)
            )
            sys.exit(os.EX_OK)

        # Look for response in positional args
        try:
            response = positional_args[0]
        except IndexError:
            optparser.print_help(file=sys.stderr)
            sys.exit(3)

        return response

    #
    # Main
    #
    locale.setlocale(locale.LC_ALL, "")
    response = process_command_line()
    sys.exit(1 - rpmatch(response))

# vi: set ft=python et sw=4 ts=4:
