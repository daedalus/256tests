#!/usr/bin/env python
# Author Dario Clavijo 2016
# simple ROT13 algo or Caesar Cipher
import fileinput

def rot13(test):
	p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
	r = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM "
	d = ""
	for l in test:
		d +=  r[p.find(l)]
	return d

#print rot13(rot13("Dario Clavijo"))

for line in fileinput.input():
	print rot13(line.rstrip())
