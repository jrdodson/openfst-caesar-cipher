#! /usr/bin/python

import sys

lines = sys.stdin.readlines()

cState = 0
nState = cState+1
letters = ""
for line in lines:
	letters +=line.lower()
	for char in letters:
		if char == ' ':
			print "{0} {1} {2} {2}".format(cState, nState, "<sp>")			
		else:
			print "{0} {1} {2} {2}".format(cState, nState, char)
		cState+=1
		nState+=1

print cState



