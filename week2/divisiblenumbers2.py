"""
Write a function that receives a list of numbers
and a list of terms and returns only the elements that are divisible
by all of those terms. You must use two nested list comprehensions to solve it.

Example:
    divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])  # [12, 6]

"""

def divisible_numbers2(a_list, a_list_of_terms):
    output = [n for n in a_list if all([n % t == 0 for t in a_list_of_terms])]
    return output
