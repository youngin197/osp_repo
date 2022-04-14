#!/usr/bin/python3
#word frequency count program

import sys
import re

if __name__=='__main__':
	data = open(sys.argv[1],"r")
	f = data.readlines()
	wordlist = []
	freq = {}

	#extract words
	for lines in f:
		wordlist.extend(re.split('\W+',lines))
	keywords = sorted(list(set(wordlist))[1:])
	
	#make dictionary
	for w in keywords:
		freq[w] = wordlist.count(w)
	freq = dict(sorted(freq.items(),key=lambda item: item[1],reverse = True))
	cnt = 0

	#print
	for key, val in freq.items():
		print("{:<15}".format(key) + "{:>5}".format(val))
