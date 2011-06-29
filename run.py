#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	   run.py
#		Function: Enable command line access to the Spintax class
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

from spintax import Spintax
from optparse import OptionParser

def main():
	parser = OptionParser(usage = "usage: %prog [options] list_file_name links_file_name",
						  version = "%prog 1.0")
	parser.add_option('-m', '--method',
						dest = 'method_name',
						default = 'normal', type = 'string',
						help = "Choose which Spintax method to use.")
	parser.add_option('-b', '--bracket_type',
						dest = 'bracket_type',
						default = 'curly', type = 'string',
						help = "Choose which bracket type to use to wrap your spintax.")
	parser.add_option('-d', '--delimiter',
						dest = 'delimiter',
						default = '|', type = 'string',
						help = "Choose which delimiter to use to separate your spintax.")
	parser.add_option('-t', '--link_type',
						dest = 'link_type',
						default = 'html', type = 'string',
						help = "Choose which type of links to use for spintax.")
	parser.add_option('-l', '--link_file',
						dest = 'link_file_name',
						default = None, type = 'string',
						help = "List the path to the file containing links to be spun with the list.")
	(options, args) = parser.parse_args()

	if (len(args) != 1):
		parser.error("Wrong number of arguments.")

	try:
		if (options.method_name != None and options.bracket_type != None and options.delimiter != None):
			# Clean up the option variable names
			method_name = options.method_name
			bracket_type = options.bracket_type
			delimiter = options.delimiter
			list_file = open(args[0], 'r')
			link_file = None
			link_type = None

			spintax = Spintax()
			spin_list = []
			link_list = []

			# Convert the list File into a list to be spun
			for line in list_file:
				if len(line.strip()) > 0:
					spin_list.append(line.strip())

			# Convert the links File into a list to be spun
			if (options.link_file_name != None):
				link_type = options.link_type

				link_file = open(options.link_file_name, 'r')

				for line in link_file:
					if len(line.strip()) > 0:
						link_list.append(line.strip())

			# Determine which methods to use based on options and arguments passed
			if (method_name == 'normal' or method_name == "get_spintax"):
				print spintax.get_spintax(spin_list, spintax.get_bracket_type(bracket_type), delimiter)

			elif (method_name == 'url'):
				print spintax.get_url_version(spintax.get_spintax(spin_list, spintax.get_bracket_type(bracket_type), delimiter))

			elif (method_name == 'links'):
				print spintax.get_spun_links(spin_list, link_list, spintax.get_bracket_type(bracket_type), delimiter, link_type)

	except:
		print 'Make sure you include the correct options for the method used.'

if __name__ == '__main__':
	main()