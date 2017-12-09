#!/usr/bin/python

import os
import urllib
import time
import re

#user greeting and initial arguments
os.system('clear')
print 'Welcome to the CVE summary generator.\n'
name= raw_input( "Please give this summary project a name i.e. Intel_Vuln_21NOV17.\n" )

#Create new directory for project
print 'Creating a new project directory.\n'
#os.mkdir(name)
target= raw_input( "Please provide a URL to an article about this vulnerability. Please note: the more CVEs at this URL, the better your results will be!\n" )
os.system('clear')

#download target article
print 'Building your summary for ' +name+ '.\n'
time.sleep(3)
print 'Looking for your target article.\n'
article_retrieve = urllib.urlopen(target)
text = article_retrieve.read()
cve = re.findall(r'[A-Z]{3}\-\d{1,4}\-\d{1,5}', str(text))
list = sorted(set(cve))

for k in list:
	print ('Searching for: ' + k)
	u = urllib.urlopen('https://nvd.nist.gov/vuln/detail/' + k + '.html')
	text = u.read()
	description = re.findall(r'<p data-testid="vuln-description">+.*</p>+',
					str(text), re.I|re.M)
	print (description)
