#!/usr/bin/python

import time
import re
import sys

#Get name of article
name= raw_input( "Please give this summary project a name i.e. Intel_Vuln_21NOV17.\n" )

#scrape the named article for CVEs and make a list
print 'Scraping article for CVEs.\n'
time.sleep(3)

#Eureka!
with open('{0}.html'.format(name), "r") as f:
        line = f.read()
        cve = re.findall(r'[A-Z]{3}\-\d{1,4}\-\d{1,5}', str(line))
        my_list = sorted(set(cve))
	print (my_list)
f.close()
