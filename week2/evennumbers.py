"""
Write a function that receives a list of numbers and returns only the even
elements. You must use List comprehensions to solve it.

Example:
    evens = even_numbers([5, 4, 3, 2, 1])  # [4, 2]

"""

def even_numbers(a_list):

	output = [n for n in a_list if n % 2 == 0]
	return output
