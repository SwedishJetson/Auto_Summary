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

CVE_file = open('{0}_CVEs.txt'.format(name), "w")
for i in list:
	j = i.split()
	CVE_file.writelines(j)
	CVE_file.writelines('\n')
CVE_file.close()

with open('{0}_CVEs.txt'.format(name), "r") as f:
	
k = f.read():
        	#print (k)
		l = urllib.urlopen('https://nvd.nist.gov/vuln/detail/' + k + '.html')
		print (l)
        #CVE_file.writelines(j)
        #CVE_file.writelines('\n')
f.close()

#	cve_retrieve = urllib.urlopen('https://nvd.nist.gov/vuln/detail/' + i)
#	print (cve_retrieve)
