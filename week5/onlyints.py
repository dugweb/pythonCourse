"""
Implement an @only_int_arguments decorator for the "sum_integers(*args)" function. It must
validate that all arguments passed to the function are integers, or raise
ValueError otherwise.

NOTE: Use a class decorator, not a function.

Examples:
	sum_integers(2, 4, 6, 8)  # 20
	sum_integers("a", "b", "c")  # ValueError
"""


class only_int_arguments(object):
	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args):

		def wrapper(*args):
			for val in args:
				if (not isinstance(val, int)):
					raise(ValueError, "judist priest")
			return self.original_function(args)

		return wrapper

print "judist"


@only_int_arguments
def sum_integers(*args):
	return sum(list(args))

