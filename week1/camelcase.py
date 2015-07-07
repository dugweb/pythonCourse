"""
Write a function that receives a string and returns a camel case version of it.
Example:
    camel_case('hello world')  # Hello World
"""


def camel_case(a_string):
    output = a_string.split()

    for i, text in enumerate(output):
    	if i == 0:
    		continue

    	output[i] = text.title()

    return " ".join(output)