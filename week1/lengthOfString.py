"""
Define a function that computes the length of a given list or string
You can't use the builtin `len` function, you must use a for loop.
Example:
    length('hello')  # Should return 5
"""

def length(a_string):
    
    charArr = list(a_string)
    length = 0
    
    for i in charArr:
    	length += 1

    return length

