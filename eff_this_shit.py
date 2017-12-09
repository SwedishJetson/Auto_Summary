#!/usr/bin/python
import re, urllib

sites = 'google yahoo cnn msn'.split()

for s in sites:
	print ('Searching: ' + s)
	u = urllib.urlopen('http://' + s + '.com')
	text = u.read()
	title = re.findall(r'<title>+.*</title>+',
				str(text), re.I|re.M)
	print (title[0])
