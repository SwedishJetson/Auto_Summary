#!/bin/bash

for i in $(ls | grep -); 
	do echo $i >> summary.txt 
	echo >> summary.txt
	cat $i | grep vuln-warning-banner-content | cut -d">" -f2 | cut -d"<" -f1 >> summary.txt
	echo >> summary.txt
	cat $i | grep vuln-description | cut -d">" -f2 | cut -d"<" -f1 >> summary.txt
	echo >> summary.txt
	done
