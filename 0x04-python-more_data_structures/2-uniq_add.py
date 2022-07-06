#!/usr/bin/python3
def uni_add(my_list=[]):
	result = 0
	for x in set(my_list):
		result += x
	return result
