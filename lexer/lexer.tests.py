import unittest
from lexer import Lexer


class TestLexer(unittest.TestCase):
    def test_lexer(self):
        s = """
        1 + 1 - 6 * 7 + 9 / 4 + 4 % 2 && True || False && !0
        x =  6 
        """
        lexer = Lexer(s)
        tokens = lexer.tokenize()
        print(tokens)


if __name__ == '__main__':
    unittest.main()


