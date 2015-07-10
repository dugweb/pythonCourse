"""
Write a function that produces all the members to compute
the factorial of a number. Example:
The factorial of the number 5 is defined as: 5! = 5 x 4 x 3 x 2 x 1

The terms o compute the factorial of the number 5 are: [5, 4, 3, 2, 1].

Once you have that function write other function that will compute the
factorial using the reduce funcion (related to functiona programming).

Example:
    terms = factorial_terms(5)  # [5, 4, 3, 2, 1]
    factorial = compute_factorial(terms) # 120

"""

def factorial_terms(a_number):

	terms = [n for n in range(a_number, 0, -1)]
	return terms



def compute_factorial(terms):
	
	output = reduce((lambda x, y: x * y), terms)
	return output

