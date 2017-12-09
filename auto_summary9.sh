#!/bin/bash

#user greeting and initial arguments
echo -e "Welcome to the CVE summary generator.\r\n"
echo -e "Please give this summary project a name (i.e. Intel_Vuln_21NOV17).\r\n"
read name

#create working directory for project
echo -e "Creating a new project directory.\r\n"
mkdir ./$name
echo -e "Please provide a URL to an article about this vulnerability. Please note: the more CVEs at this URL, the better your results will be!\r\n"
read target

#primary function start
printf "\n" 
echo -e "Building your summary for" $name".\r\n"
sleep 3
echo -e "Looking for your target article.\r\n"
curl "$target" > $name.html
printf "\n"
echo -e "Article downloaded!\r\n"

#scrape article for CVEs and make a list
echo -e "Scraping article for CVEs.\r\n"
sleep 3
cat $name.html | grep 'CVE-[0-9]\{4\}-[0-9]\{1,6\}' | cut -d">" -f2 | cut -d"<" -f1 | sort -u | grep -v " "| grep -v "*" | egrep '^.{1,14}$' > CVE_list.txt
cve_count=$(cat CVE_list.txt | wc -l)
echo -e "CVE list created!" $cve_count "CVEs scraped.\r\n"

#download NVD articles on the CVEs
echo -e "Pulling information on your CVEs from the Google Machine.\r\n"
sleep 3
for i in $(cat CVE_list.txt); do curl "https://nvd.nist.gov/vuln/detail/$i" > $i.html; done
article_count=$(ls | grep html | grep CVE | wc -l)
printf "\n"
echo -e "Downloaded" $article_count /$cve_count "CVE pages.\r\n"
sleep 3

#Build summary document
timestamp=$(date)
echo -e "Compiling a summary file.\r\n"
echo -e "$name Summary File\r\n" > summary.txt
echo -e "Report completed at" $timestamp".\r\n" >> summary.txt
echo >> summary.txt
echo >> summary.txt
for i in $(ls | grep html | grep CVE); 
	do echo $i >> summary.txt 
	echo >> summary.txt
	cat $i | grep vuln-warning-banner-content | cut -d">" -f2 | cut -d"<" -f1 >> summary.txt
	echo >> summary.txt
	cat $i | grep vuln-description | cut -d">" -f2 | cut -d"<" -f1 >> summary.txt
	echo >> summary.txt
	done

#directory cleanup
echo -e "Cleaning up the results.\r\n"
mv *.html ./$name/
mv *.txt ./$name/

#Closeout
echo -e "Project complete!\r\n"
read -r -p "Do you want to read the report now? [Y/N]..." option1
if [[ "$option1" =~ ^([yY]|[yY])+$ ]]
then
	cat $name/summary.txt
else	
	printf "\n"
	echo -e "Your results can be found at $name/summary.txt.\r\n"
fi
