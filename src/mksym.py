#! /usr/bin/python
#  John Ryan Dodson

counter = 0
print "{0} {1}".format("<eps>", counter)
counter+=1
print "{0} {1}".format("<sp>", counter)

for i in range(ord('a'), ord('z')+1):
	counter+=1
	print "{0} {1}".format(chr(i), counter)	
