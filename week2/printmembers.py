"""
Write a function that receives a list and prints all its
items using a list comprehension.

Example:
    print_members(["Hello", 3, True, (1, 2)])

"""

# since python 2.* print is a statement, not a function and
# doesn't work in comprehensions (at least not the way I was using it)
from __future__ import print_function

def print_members(a_list):
    
    f = lambda x: print(x)
    [f(a) for a in a_list]
