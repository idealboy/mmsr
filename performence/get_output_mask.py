import os
import sys

op_name = []

with open("name.txt") as lines:
	for line in lines:
		line = line.strip()
		if "conv" in line or "add" in line:
			print 1
		else:
			print 0
