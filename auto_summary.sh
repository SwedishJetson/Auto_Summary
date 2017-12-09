#!/bin/bash

echo -e "Welcome to S747IK's totally sweet vulnerability summary generator.\r\n"
echo -e "Please provide the URL to the writeup you are interested in.\r\n"
read target
echo -e "You have chosen" $target "as your targeted writeup.\r\n"
echo "Starting process."
sleep 2
clear
curl "$target" > $target.html
echo -e "Target page has been downloaded.\r\n"
echo -e "Scraping article for CVEs.\r\n"
cat $target.html | grep CVE > $target_CVE_list.txt
echo -e "CVE list complete!\r\n"
