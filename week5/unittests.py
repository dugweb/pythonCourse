"""
Implement one unit tests for "add(a, b)" function, that validates the resulting
value of its execution.
"""


def add(a, b):
    return a + b
    

import unittest    
class AssignmentTestCase(unittest.TestCase):
  
    def test_add(self):
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(9383, -38372), -28989)
        pass