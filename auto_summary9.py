#!/usr/bin/python

import os
import urllib2
import time
import re

#user greeting and initial arguments

os.system('clear')
print
print 'Welcome to the CVE summary generator.\n'
name= raw_input( "Please give this summary project a name i.e. Intel_Vuln_21NOV17.\n" )
print

#Create new directory for project
print 'Creating a new project directory.\n'
os.mkdir(name)
target= raw_input( "Please provide a URL to an article about this vulnerability. Please note: the more CVEs at this URL, the better your results will be!\n" )

#clipboard
#print '\n'

#download target article
print 'Building your summary for ' +name+ '.\n'
time.sleep(3)
print 'Looking for your target article.\n'
target_retrieve = urllib2.urlopen(target)
target_article = open('{0}.html'.format(name),"w")
target_article.writelines(target_retrieve.read())
target_article.close()
print 'Target article downloaded!\n'

#scrape article for CVEs and make a list
#print 'Scraping article for CVEs.\n'
#time.sleep(3)

#with open('{0}.html'.format(name)) as origin_file:
#    for line in origin_file:
#        line = re.findall(r'CVE', line)
#        if line:
#           line = line[0].split('>')[1]
#        print line
