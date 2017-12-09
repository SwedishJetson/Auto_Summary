#!/bin/bash

echo -e "Welcome to S747IK's totally sweet vulnerability summary generator.\r\n"
echo -e "Please give this summary a name (i.e. intel_vuln_21NOV17).\r\n"
read name
echo -e "Creating a new project directory.\r\n"
mkdir ./$name
echo -e "Please provide the URL for which you are interested.\r\n"
read target
echo -e "Building your summary for" $name ".\r\n"
sleep 2
clear
curl "$target" > ./$name/$name.html
echo -e "Scraping article for CVEs.\r\n"
cat ./$name/$name.html | grep 'CVE-[0-9]\{4\}-[0-9]\{4\}' | cut -d">" -f2 | cut -d"<" -f1 | sort -u | grep -v " " | egrep '^.{1,13}$' > ./$name/CVE_list.txt
echo -e "CVE list complete!\r\n"
echo -e "Downloading information on pertinent CVEs.\r\n"
sleep 2
clear
for i in $(cat ./$name/CVE_list.txt); do curl "https://nvd.nist.gov/vuln/detail/$i" > ./$name/$i.html; done
echo -e "Downloads complete!\r\n"
sleep 2
clear
echo -e "Compiling a summary file.\r\n"
for i in $(ls ./$name/ | grep -); 
	do echo $i >> ./$name/summary.txt 
	echo >> ./$name/summary.txt
	cat $i | grep vuln-warning-banner-content | cut -d">" -f2 | cut -d"<" -f1 >> ./$name/summary.txt
	echo >> ./$name/summary.txt
	cat $i | grep vuln-description | cut -d">" -f2 | cut -d"<" -f1 >> ./$name/summary.txt
	echo >> ./$name/summary.txt
	done
