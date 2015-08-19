"""
Write a function, that receives the path to a text file that contains JUST ONE word
per line, and returns a dictionary with the counter of words starting with each
letter from 'a' to 'z'.

Example:
  counter_by_letter('words.txt')  
  # {
	'a': 2,
	'b': 10,
	'c': 0,
	...
	'z': 1
  }

"""


def counter_by_letter(filepath):
	
	f = open(filepath, 'r')
	lines = f.readlines()
	output = {}

	for val in lines:
		val = val.lower().strip()
		
		key = val[0]

		if key in output:
			output[key] += 1
		else:
			output[key] = 0

	return output
