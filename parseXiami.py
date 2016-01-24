# use to parse xiami source file and get song lists

import re

pattern = re.compile('href="http://www.xiami.com/song/[^>]+>([^<]+)</a>')

with open("f.html") as fp:
	for line in fp:
		match = pattern.match(line)
		if match:
			print match.group()
