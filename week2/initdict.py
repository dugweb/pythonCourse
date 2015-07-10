"""
Write a function that receives a list and
returns a dictionary with the elements initialized with the value 0.

You MUST use dict comprehensions.

Example:
    init_dict(['a', 'b', 'c']) # {'a': 0, 'b': 0, 'c': 0}

"""

def init_dict(a_list):

	return {a:0 for a in a_list}