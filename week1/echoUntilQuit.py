"""
Define a function that asks for a string and echoes it back
until the input 'quit' is provided.
Example:
    echo()
    > Insert a string: hello
    > hello
    > Insert a string: world
    > world
    > Insert a string: quit
    > bye!
"""

def echo():
    
    user_input = ""

    while user_input.lower() != "quit":
    	user_input = raw_input("Insert a string: ")
    	print "{}".format(user_input)

    print "bye!"