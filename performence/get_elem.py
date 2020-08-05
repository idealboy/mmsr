import os
import sys


with open("output_shape.txt") as lines:
	for line in lines:
		line = line.strip()
		items = line.split("#")
		num = 0
		for item in items:
			shape = [int(s) for s in item.split("[")[1].split("]")[0].split(",")]
			elem = 1
			for s in shape:
				elem = elem * s
			num = num + elem
		print num
		
