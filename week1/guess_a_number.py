"""
Write a program that generates a secret random number and asks the user to guess it.
It should count how many attempts were made before the number is guessed.
The program must also give hints to the user.
Example:
    python guess_a_number.py
    > Guess your number
    > 3
    > Wrong! Try with a larger one
    > 5
    > Wrong! Try with a smaller one
    > 4
    > You guessed correctly! The number was 4 indeed!
"""
import random

def guess_a_number():
    
    num = random.randint(1, 100)
    guess = 0
    
    while guess != num:

    	if (guess == 0):
    		guess = convert_to_int(raw_input("Guess your number: "))
    	elif (guess > num):
    		guess = convert_to_int(raw_input("Wrong! Try with a smaller one: "))
    	else:
    		guess = convert_to_int(raw_input("Wrong! Try with a larger one: "))

    print "You guessed correctly! The number was {} indeed!".format(guess)

def convert_to_int(s):
	try:
		ret = int(s)
	except ValueError:
		ret = "not an int"
	return ret