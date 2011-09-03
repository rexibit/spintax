#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#		spintax.py
#		Function: Manage Spintax
#		Github Repository URL: https://github.com/rexibit/spintax
#
#	   Copyright 2011 Matthew Watts <matthew@rexibit.com>
#
#	   This program is free software; you can redistribute it and/or modify
#	   it under the terms of the GNU General Public License as published by
#	   the Free Software Foundation; either version 2 of the License, or
#	   (at your option) any later version.
#
#	   This program is distributed in the hope that it will be useful,
#	   but WITHOUT ANY WARRANTY; without even the implied warranty of
#	   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	   GNU General Public License for more details.
#
#	   You should have received a copy of the GNU General Public License
#	   along with this program; if not, write to the Free Software
#	   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#	   MA 02110-1301, USA.
#
#

import re
import random
from string import Template

class Spintax:
	def get_spintax(self, list_to_spin, bracket_list, delimiter):
		spun_string = ''

		# Ensure method arguments are lists, then build the spun string
		try:
			if (isinstance(list_to_spin, list) and isinstance(bracket_list, list) and isinstance(delimiter, basestring)):
				for item in list_to_spin:
					if (item == list_to_spin[0]):
						spun_string += str(bracket_list[0]) + str(item) + delimiter
					elif (item != list_to_spin[-1]):
						spun_string += str(item) + delimiter
					else:
						spun_string += str(item) + str(bracket_list[1])

			return spun_string

		except TypeError:
			raise 'Arguments should contain two lists and a string.'

	def get_spun_links(self, list_to_spin, links_to_spin, bracket_list, delimiter, link_type):
		spun_string = self.get_spintax(list_to_spin, bracket_list, delimiter)
		spun_link = ''

		# Ensure method arguments are lists, then build the spun strings
		try:
			if (isinstance(links_to_spin, list) and isinstance(link_type, basestring)):
				for item in links_to_spin:
					if (item == links_to_spin[0]):
						spun_link += str(bracket_list[0]) + str(item) + delimiter
					elif (item != links_to_spin[-1]):
						spun_link += str(item) + delimiter
					else:
						spun_link += str(item) + str(bracket_list[1])

			return self.get_link(link_type, spun_string, spun_link)

		except TypeError:
			raise 'Arguments should contain three lists and two strings.'

	# Unspin spintax
	def unspin(self, spun_string, delimiter):
		while True:
			spun_string, n = re.subn('{([^{}]*)}',
						   lambda m: random.choice(m.group(1).split(delimiter)),
						   spun_string)
			if n == 0:
				break

		return spun_string.strip()

	# A dictionary of all the types of brackets
	def get_bracket_type(self, bracket_type_name):
		bracket_types = {
							'curly': ['{', '}'],
							'angle': ['<', '>'],
							'square': ['[', ']'],
							'none': ['', '']
						}

		try:
			return bracket_types[bracket_type_name]

		except:
			raise 'There is no bracket type by that name.'

	# Convert a spun string to be URL friendly
	def get_url_version(self, spun_string):
		try:
			spun_string = spun_string.lower()
			spun_string = re.sub(" ", "-", spun_string)

			return spun_string

		except:
			raise 'There was an error with the passed spun string, Be sure to only include alpha-numeric characters and spaces.'

	# A dictionary of all the link types
	# Returns a formatted link of the passed link type
	def get_link(self, link_type, string, link):
		link_types = {
						'html': ['angle', '${start}a href="${url}"${end}${anchor}${start}/a${end}'],
						'bbcode': ['square', '${start}url=${url}${end}${anchor}${start}/url${end}'],
						'scrapebox': ['none', '${url} ${anchor}'],
						'senuke': ['none', '${url}##${anchor}']
					 }

		link_type = link_types[link_type]
		brackets = self.get_bracket_type(link_type[0])
		formatted_link = Template(link_type[1])

		return formatted_link.substitute(start=brackets[0], end=brackets[1], anchor=string, url=link)