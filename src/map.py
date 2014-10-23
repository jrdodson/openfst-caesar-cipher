#! /usr/bin/python
#  John Ryan Dodson

import sys

shift = int(sys.stdin.read())

alpha=[]
for item in range(ord('a'), ord('z')+1):
	alpha.append(chr(item))
print "{0} {0} {1} {1}".format(0, "<sp>")
for i in range(0,len(alpha)):
	ch = (i+shift)%26
	print "{0} {0} {1} {2}".format(0, alpha[i], alpha[ch])

print 0
