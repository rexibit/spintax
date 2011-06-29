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

from setuptools import setup, find_packages

DESCRIPTION = 'Spintax Management Utility'
LONG_DESCRIPTION = None

try:
	LONG_DESCRIPTION = open('README.txt').read()
except:
	pass

CLASSIFIERS = [
	'Development Status :: 1 - Beta',
	'Intended Audience :: Developers',
	'Operating System :: OS Independent',
	'Programming Language :: Python',
	'Framework :: None',
	'Topic :: Data Management',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'License :: GNU General Public License :: BSD license',
]

setup(name = 'Spintax',
	packages = find_packages(),
	author = 'Matthew Watts',
	author_email = 'matthew@rexibit.com',
	url = 'https://github.com/rexibit/spintax',
	description = DESCRIPTION,
	long_description = LONG_DESCRIPTION,
	platforms = ['any'],
	classifiers = CLASSIFIERS,
	install_requires = [],
	version = '1.0',
)