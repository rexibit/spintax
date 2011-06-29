#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       setup.py
#		Function: Setup the spintax module
#		Github Repository URL: https://github.com/rexibit/spintax
#
#       Copyright 2011 Matthew Watts <matthew@rexibit.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
#

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

DESCRIPTION = 'Spintax Management Utility'
LONG_DESCRIPTION = None

try:
	LONG_DESCRIPTION = read('README.txt')
except:
	pass

CLASSIFIERS = [
	'Intended Audience :: Developers',
	'Operating System :: OS Independent',
	'Programming Language :: Python',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'License :: OSI License :: BSD license',
]

setup(name = 'Spintax',
	packages = ['spintax'],
	author = 'Matthew Watts',
	author_email = 'matthew@rexibit.com',
	url = 'https://github.com/rexibit/spintax',
	description = DESCRIPTION,
	long_description = LONG_DESCRIPTION,
	classifiers = CLASSIFIERS,
	version = '1.0.1',
)