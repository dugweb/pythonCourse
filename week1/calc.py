"""
Write a function that receives 2 numbers and performs simple calculations
(additions, subtractions, multiplications and divisions)
based on a string parameter.
Example:
    calculator(2, 3, 'add')       # Should return 5
    calculator(7, 3, 'subtract')  # Should return 4
    calculator(2, 7, 'multiply')  # Should return 14
    calculator(8, 4, 'divide')    # Should return 2
    calculator(5, 2, 'divide')    # Should return 2.5 ATTENTION!
"""
import operator

def calculator(param1, param2, operation):
    
	operations = {
		"add"		: operator.add,
		"subtract"	: operator.sub,
		'multiply'	: operator.mul,
		'divide'	: operator.div
	}

	return operations[operation](float(param1), float(param2))

