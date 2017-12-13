#!/usr/bin/python

import os
import urllib
import time
import sys
import re

#user greeting and initial arguments
os.system('clear')
todaysdate = time.strftime("%c")
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
with open('{0}.html'.format(name), "w") as f:
	article_retrieve = urllib.urlopen(target)
	f.writelines(article_retrieve.read())
f.close()
print 'Your article has been downloaded.\n'
time.sleep(3)
os.system('clear')

#scrape the named article for CVEs and make a list
print 'Scraping article for CVEs.\n'
time.sleep(3)
with open('{0}.html'.format(name), "r") as f:
        line = f.read()
        cve = re.findall(r'[A-Z]{3}\-\d{1,4}\-\d{1,5}', str(line))
        my_list = sorted(set(cve))
	c = len(my_list)
f.close()

#Download scraped CVEs
print 'CVEs scraped from target article: ', c, '\n'
time.sleep(3)
os.system('clear')
for k in my_list:
	print ('Searching for: ' + k + '\n')
	with open('{0}.html'.format(k), "w") as a:
		u = urllib.urlopen('https://nvd.nist.gov/vuln/detail/' + k)
		a.writelines(u.read())
	a.close()
	print k + ' downloaded.\n'

with open('{0}_summary.txt'.format(name), "w") as f:
        f.write('Auto Summary for ' +name+ '.\n\n')
        f.write('Proejct initiated at: ' +todaysdate+ '.\n\n')
        for k in my_list:
                with open('{0}.html'.format(k), "r") as a:
                        line = a.read()
                        description = re.findall(r'<p data-testid="vuln-description">+.*</p>+', str(line))
                        f.writelines(k+'\n')
                        f.writelines('\n')
                        f.writelines(str(description)+'\n')
                        f.writelines('\n')
                a.close()
        	print k + ' summarized.\n'
f.close()


