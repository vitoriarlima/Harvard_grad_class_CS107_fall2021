#!/bin/bash


grep -c '[[:digit:]]' apollo13.txt > apollo_out.txt  
grep --help | grep '\-\-count'
ls *.py | wc -l
find . -type f ! -perm /o=w,o=r
find . -type f,d ! -perm /o=w,o=r




