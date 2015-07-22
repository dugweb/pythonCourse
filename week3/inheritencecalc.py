"""
You'll need to build a better version of your calculator using OOP and inheritance:
A calculator can be built with different operations. An Operation is an abstract class for which you'll define
subclasses.

Example:

calc1 = Calculator(operations={
    'add': AddOperation,
    'subtract': SubtractOperation})

calc2 = Calculator(operations={
    'add': AddOperation})

The calculator has 1 generic method `calculate` that will receive the arguments
and the operation to perform. For example:

calc1.calculate(2, 1, 5, 'add')  # Should return 2 + 1 + 5 = 8
calc2.calculate(1, 5, 'add')  # Should return 1 + 5 = 6

*IMPORTANT: The number of arguments should be variable*

The Calculator will check if it has that computation present and
invoke the operation. Operations are initialized with the arguments to compute:

op = AddOperation(2, 1, 5)

Once you have an operation object created you should be able to invoke the `operate`
method PRESENT IN EVERY OPERATION.

op.operate()  # Should return 8

*Important notes:*
* The only method that you must implement for every operation (descendant from Operation)  is the `operate` method.
* If the operation is not supported by the calculator (for exampleinvoking `multiply` on calc1)
   the calculator should raise a custom exception (built by you) named `OperationInvalidException`.

This is a unittest class that might be useful for development:


class CalculatorTestCase(unittest.TestCase):
    def test_calculator_with_one_operation(self):
        calc = Calculator(operations={
            'add': AddOperation})
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)

    def test_calculator_invoked_with_an_invalid_operation(self):
        calc = Calculator(operations={
            'add': AddOperation})
        with self.assertRaises(OperationInvalidException):
            res = calc.calculate(1, 5, 13, 2, 'INVALID')


class AddOperationTestCase(unittest.TestCase):
    def test_add_operation_with_multiple_arguments(self):
        op = AddOperation(5, 1, 8, 3, 2)
        self.assertEqual(op.operate(), 19)

    def test_add_operation_with_1_arguments(self):
        op = AddOperation(5)
        self.assertEqual(op.operate(), 5)


if __name__ == '__main__':
    unittest.main()

"""

class Operation(object):
    def __init__(self, *args):
        # Do something here
        pass

    def operate(self):
        raise NotImplementedError()

class AddOperation(object):
    # The only method present in this class
    def operate(self):
        pass


class SubtractOperation(object):
    def operate(self):
        pass

class Calculator(object):
    pass