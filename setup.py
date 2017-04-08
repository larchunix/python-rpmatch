#!/hint/python -tt
# -*- coding: UTF-8 -*-

# This script is free software, and you may redistribute it and/or modify
# it under the same terms as Python itself.

from distutils.core import setup

setup(
  name='rpmatch',
  description='Python implementation of rpmatch(3) libc function',
  author='Denis Ollier',
  license='GPL-3.0-or-later',
  version='1.0.0',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ],
  py_modules=['rpmatch'],
)

# vi: set ft=python et sw=4 ts=4:
