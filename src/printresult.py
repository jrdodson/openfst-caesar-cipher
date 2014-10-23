#! /usr/bin/python
#  John Ryan Dodson

import sys

lines = sys.stdin.readlines()
result=""
for line in lines:
	temp = line.split()
	if temp[len(temp)-1].isalpha():
		result+=temp[len(temp)-1]
	else:
		result+= " "
print result

