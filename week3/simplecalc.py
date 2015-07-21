"""
Build a simple calculator using Object Oriented Programming.
This is the interface it should follow:

    calculator = Calculator()

    calculator.add(2, 4)  # 6
    calculator.subtract(8, 1)  # 7
    calculator.multiply(3, 5)  # 15
    calculator.divide(5, 2)  # 2.5
"""

class Calculator(object):
    
    @classmethod
    def add(self, num1, num2):
        return float(num1) + float(num2)
    
    @classmethod
    def subtract(self, num1, num2):
        return self.add(num1, num2 * -1)
    
    @classmethod
    def multiply(self, num1, num2):
        return float(num1) * float(num2)
    
    @classmethod
    def divide(self, num1, num2):
        return float(num1) / float(num2)
    