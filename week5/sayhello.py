"""
Implement unit tests for "say_hello()" function. Each unit test function inside
AssignmentTestCase class must follow the behavior described in the function docstring.
"""


def say_hello(name=None):
    if not name:
        raise ValueError("We need a name.")
    return "Hello {}".format(name)
    

import unittest    
class AssignmentTestCase(unittest.TestCase):
  
    def test_say_hello(self):
        """Should say hello when given name is valid"""
        self.assertTrue(say_hello('doug'))
        
        
    def test_say_hello_with_no_name(self):
        """Should raise ValueError when no name is given"""
        self.assertRaises(ValueError, say_hello)


unittest.main()