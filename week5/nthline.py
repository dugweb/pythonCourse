"""
Write a function, that receives a path to a text file and a line number as parameter, 
and returns the N-th line of that file.

Example:
  read_line_number('test-file.txt', 2)  # "this is the line number 2"

"""


def read_line_number(filepath, line_number):
    thefile = open(filepath, 'r')
    return thefile.readlines()[line_number]