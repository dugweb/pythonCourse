"""
Write a function, that receives a path to a text file as first parameter and
a list of string as second one. The function should write each string in a new
line of the text file. If 5 strings are given in the list, the resulting file
should have 5 lines.

Example:
  write_lines('test-file.txt', ['hello', 'world'])

"""


def write_lines(filepath, list_of_strings):
	
	try:
		f = open(filepath, 'r+')
	except:
		f = open(filepath, 'w')

	for line in list_of_strings:
		f.write(line + "\n")

	f.close()
	return
