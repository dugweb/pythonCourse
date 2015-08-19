"""
Write a function, that receives a path to a text file as parameter, 
and returns the amount of lines that text file has.

Example:
  count_lines('test-file.txt')  # 10

"""


def count_lines(filepath):
    f = open(filepath, 'r')
    return len(f.readlines())