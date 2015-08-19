"""
Write a function, that receives a path to a text file as parameter, 
and returns the first line of that file.

Example:
  read_file('test-file.txt')  # "this is the first line"

"""


def read_file(filepath):

	thefile = open(filepath, 'r')
	return thefile.readline()