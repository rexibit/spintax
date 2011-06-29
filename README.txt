**Spintax**

Spintax is a great way to mad-lib or easily alter parts of text for reuse.
It's too bad that more people don't make use of it. That's where this class comes in!

**About**

Spintax is developed using Python 2.7 and hasn't been tested in prior versions.
It is basically a port and clean up of the PHP methods used on http://www.getspintax.com

Github Repository URL: https://github.com/rexibit/Spintax

**Use**

The Spintax class currently has these methods:
- ``get_spintax``, takes a list of strings and converts it to a spun string using the bracket list
 and delimiter specified when called.

	::
		spintax = Spintax()

		# Get your text to be spun from a file, text area, etc. and store it into a list
		list_to_spin = []

		# Get your bracket list from the ``get_bracket_type`` method
		bracket_list = spintax.get_bracket_type('curly')

		# Specify the delimiter string
		delimiter_string = '|'

		spun_string = spintax.get_spintax(list_to_spin, bracket_list, delimiter_string)

		# Outputs: {text part 1|text part 2|text part 3|...}
		print spun_string

- ``get_spun_links``, takes a list of strings and a list of URLs and converts to a spun string using
 the bracket list, delimiter, and link type specified when called.

	::
		spintax = Spintax()

		# Get your text to be spun from a file, text area, etc. and store it into a list
		list_to_spin = []

		# Get your URLs to be spun from a file, text area, etc. and store it into a list
		links_to_spin = []

		# Get your bracket list from the ``get_bracket_type`` method
		bracket_list = spintax.get_bracket_type('curly')

		# Specify the delimiter string
		delimiter_string = '|'

		# Specify the type of link you want outputted
		link_type_string = 'html'

		spun_string = spintax.get_spun_links(list_to_spin, links_to_spin, bracket_list,
											delimiter_string, link_type_string)

		# Outputs: <a href="{http://www.example1.com|http://www.example2.com|http://www.example3.com|
		#...}">{text part 1|text part 2|text part 3|...}</a>

		print spun_string

- ``unspin``, unspins a string that contains spintax

	::
		spintax = Spintax()

		spun_string = '<a href="{http://www.example1.com|http://www.example2.com|http://www.example3.com|
		...}">{text part 1|text part 2|text part 3|...}</a>'

		# Outputs a random string and URL, <a href="http://www.example2.com">text part 3</a>
		print spintax.unspin(spun_string)

- ``get_bracket_type``, takes a string and returns a list for the opening and closing brackets of the type

	::
		spintax = Spintax()

		# Possible Types (strings): curly, angle, square, none
		bracket_type_string = 'angle'

		# Outputs: [<, >]
		print spintax.get_bracket_type(bracket_type_string)

- ``get_url_version``, takes a spun string and returns it in lowercase with spaces replaced by -

	::
		spintax = Spintax()

		spun_string = '{text part 1|text part 2|text part 3}'

		#Outputs: {text-part-1|text-part-2|text-part-3}
		print spintax.get_url_version(spun_string)

- ``get_link``, takes 3 strings: one for the type of link, one for the string, one for the URL,
 and returns a formatted link based on the type chosen.
You can also customize new link types by using string Templates and adding to the dictionary in this method.

	::
		spintax = Spintax()

		string = 'text part 1'
		url_string = 'http://www.example1.com'

		# Possible Types (strings): html, bbcode, scrapebox, senuke
		link_type_string = 'html'

		#Outputs: <a href="http://www.example1.com">text part 1</a>
		print spintax.get_link(link_type_string, string, url_string)

**Command Link Run Script**

The Spintax class is very versatile, but if you just want to quickly spin something from a text file, the run.py script is it.

List of Options

	::
		-m, --method : lists the type of spin you want (normal, links, url)

		-b, --bracket_type : the bracket type you want to use, default is "curly"

		-d, --delimiter : the delimiter you want to use, default is "|"

		-t, --link_type : the link type you want to use, default is "html"

		-l, --link_file : the path to the link file you want to use

Examples

- Print out a spun list
	::
		$ python run.py "/path/to/list/file/list.txt"
		$ {text part 1|text part 2|text part 3}

- Print out a spun list in URL format
	::
		$ python run.py -m url "/path/to/list/file/list.txt"
		$ {text-part-1|text-part-2|text-part-3}

- Print out a spun list of links
	::
		$ python run.py -m links -l "/path/to/links/file/links.txt" "/path/to/list/file/list.txt"
		$ <a href="{http://www.example1.com|http://www.example2.com|http://www.example3.com
		">{text part 1|text part 2|text part 3}</a>