"""
Implement a @small_arguments decorator for the "sum(a, b)" function, 
that raises ValueError if any of given arguments are greater than 10.

Examples:
    sum(2, 4)  # 6
    sum(11, 4)  # ValueError
"""


def small_arguments(original_function):
    
	def inner(a, b):
		if (a > 10 or b > 10):
			raise ValueError('cannot sum more than 10')
	
		return original_function(a, b)

	return inner


@small_arguments
def sum(a, b):
	return a + b