"""
Write a function that combines list comprehensions and lambdas
to transform temperatures given in celsius to fahrenheit.

Example:
	to_fahrenheit([0, 10, 25, 30, 100]) # [32.0, 50.0, 77.0, 86.0, 212.0]

"""

def to_fahrenheit(a_list):
	f = lambda c: c * 1.8 + 32
	output = [f(c) for c in a_list]
	return output