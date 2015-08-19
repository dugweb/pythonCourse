"""
Implement a @pretty_result decorator for the "sum(a, b)" function, that returns 
the result with this layout: "The result of the sum is: XXX"

Examples:
    sum(11, 4)  # "The result of the sum is: 15"
"""


def pretty_result(original_function):

	def result(x, y):
		return "The result of the sum is: {}".format(original_function(x, y))

	return result



@pretty_result
def sum(a, b):
	return a + b