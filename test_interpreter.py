import unittest
from lexer import Lexer
from myParser import Parser
from interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    def test_arithmetic(self):
        source_code = "3 + 4"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, 7)
        print(result)

    def test_simple_number(self):
        source_code = "42%3"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, 0)
        print(result)

    def test_parentheses(self):
        source_code = "(3 + 4) * (2 - 1)"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, 7)
        print(result)

    def test_boolean_operations(self):
        source_code = "True and False"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, False)

        source_code = "True or False"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, True)

    def test_comparison_operations(self):
        source_code = "3 > 4"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, False)

        source_code = "3 < 4"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, True)

    def test_unary_operations(self):
        source_code = "-5 + 3"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, -2)

    def test_function_definition_and_application(self):
        # Define a recursive function to compute the factorial of a number
        source_code = """
        Defun factorial(n)
        ((n == 0) or (n * factorial(n - 1)))
        factorial(5)
        """
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, 120)

    def test_lambda_expression(self):
        # Define a Lambda expression to perform an addition of 2 numbers
        source_code = "(Lambd x. (Lambd y. (x + y)))(3)(4)"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, 7)

    def test_fibonacci(self):
        # Define a recursive function to compute the nth Fibonacci number
        source_code = """
        Defun fibonacci(n)
        ((n <= 1) or (fibonacci(n - 1) + fibonacci(n - 2)))
        fibonacci(10)
        """
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, 89)
        print(result)

    def test_sum_to_n(self):
        # Define a function to compute the sum of numbers from 1 to n
        source_code = """
        Defun sum_to_n(n)
        ((n == 1) or (n + sum_to_n(n - 1)))
        sum_to_n(10)
        """
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, 55)
        print(result)

    def test_is_even(self):
        # Define a function to check if a number is even
        source_code = """
        Defun is_even(n)
        ((n % 2) == 0)
        is_even(4)
        """
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, True)

        source_code = """
        is_even(5)
        """
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, False)

    def test_countdown(self):
        # Define a function to simulate a "while loop" using recursion
        source_code = """
        Defun countdown(n)
        (n == 0) or (n and countdown(n - 1))
        countdown(5)
        """
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        self.assertEqual(result, 0)
        print(result)

if __name__ == '__main__':
    unittest.main()
