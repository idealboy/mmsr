import os
import sys

op_name = []
with open("name.txt") as lines:
	for line in lines:
		line = line.strip()
		op_name.append(line)

with open("shape.txt") as lines:
	index = 0
	for line in lines:
		name = op_name[index]
		line = line.strip()
		items = line.split("\t")
		if "conv" in name:
			input_shape = [int(s) for s in items[0].split("#")[0].split("[")[1].split("]")[0].split(",")]
			weight_shape = [int(s) for s in items[0].split("#")[1].split("[")[1].split("]")[0].split(",")]
			output_shape = [int(s) for s in items[1].split("[")[1].split("]")[0].split(",")]
			flops = output_shape[0] * output_shape[1] * output_shape[2] * output_shape[3] * weight_shape[0] * weight_shape[1] * weight_shape[2] * 2
		elif "add" in name:
			output_shape = [int(s) for s in items[1].split("[")[1].split("]")[0].split(",")]
			flops = output_shape[0] * output_shape[1] * output_shape[2] * output_shape[3]
		else:
			flops = 0
		print flops
			
		index+=1
