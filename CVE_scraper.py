#!/usr/bin/python

import time
import re
import sys

#Get name of article
name= raw_input( "Please give this summary project a name i.e. Intel_Vuln_21NOV17.\n" )

#scrape the named article for CVEs and make a list
print 'Scraping article for CVEs.\n'
time.sleep(3)

#this gets me close...
#with open('{0}.html'.format(name), "r") as f:
#	for line in f:
#		if re.search("CVE-", line):
#			print line
#f.close()

#nest re.search statements to "grep" and "cut"
#with open('{0}.html'.format(name), "r") as f:
#       for line in f:
#		if re.search("CVE-", line):
#			if re.search('>', line):
#				line.split('\>')[1]
#			else:
#				print line
#f.close()

greppy = r"^.([A-Z]\{3\}\[0-9]\{4\}\[0-9]\{4\})+$"
with open('{0}.html'.format(name), "r") as f:
	for line in f:	
		CVE = re.search(greppy, "CVE")
		if CVE:
			print CVE
		else:
			print 'sheisse'
f.close()
