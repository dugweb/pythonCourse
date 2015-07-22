"""
Write a simple random password generator using iterators. The generator can accept two parameters:
* available_chars: The characters to use to generate the password. OPTIONAL. Default: A set of characters, digits and symbols. (hint, check the string module)
* length: The length of the password. OPTIONAL. Default: 8

pass_generator = SimplePasswordGenerator()
next(pass_generator)  # %58a$d8a (length=8)

pass_generator = SimplePasswordGenerator()
next(pass_generator)  # '%58a$d8a' (length=8)

pass_generator = SimplePasswordGenerator(available_chars=['a', 'b'], length=4)
next(pass_generator)  # 'abba'

"""

import string
import random

class SimplePasswordGenerator():

	def __init__(self, length = 8, available_chars = string.ascii_letters + string.digits + string.punctuation):
		self.length = length
		self.characters = available_chars

	def __iter__(self):
		return self

	def __next__(self):
		password = ""
		for i in range(self.length):
			password += random.choice(self.characters)
		return password

	def next(self):
		
		return self.__next__()


pass_generator = SimplePasswordGenerator()
next(pass_generator)  # %58a$d8a (length=8)

pass_generator = SimplePasswordGenerator()
next(pass_generator)  # '%58a$d8a' (length=8)

pass_generator = SimplePasswordGenerator(available_chars=['a', 'b'], length=4)
next(pass_generator)  # 'abba'

