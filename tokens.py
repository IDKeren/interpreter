# tokens.py
# This file defines the token types and keywords used by the lexer and parser.

# Token types
TT_INT = 'INT'           # Integer numbers
TT_FLOAT = 'FLOAT'       # Floating-point numbers
TT_PLUS = 'PLUS'         # Addition (+)
TT_MINUS = 'MINUS'       # Subtraction (-)
TT_MUL = 'MUL'           # Multiplication (*)
TT_DIV = 'DIV'           # Division (/)
TT_MOD = 'MOD'           # Modulo (%)
TT_LPAREN = 'LPAREN'     # Left parenthesis '('
TT_RPAREN = 'RPAREN'     # Right parenthesis ')'
TT_IDENTIFIER = 'IDENTIFIER'  # Variable names and function names
TT_KEYWORD = 'KEYWORD'   # Reserved keywords (Defun, Lambd, etc.)
TT_EQ = 'EQ'             # Equality (==)
TT_NEQ = 'NEQ'           # Not equal (!=)
TT_GT = 'GT'             # Greater than (>)
TT_LT = 'LT'             # Less than (<)
TT_GTE = 'GTE'           # Greater than or equal to (>=)
TT_LTE = 'LTE'           # Less than or equal to (<=)
TT_AND = 'AND'           # Logical AND (&&)
TT_OR = 'OR'             # Logical OR (||)
TT_NOT = 'NOT'           # Logical NOT (!)
TT_COMMA = 'COMMA'       # Comma (,) used in function arguments
TT_DOT = 'DOT'           # Dot (.) used in lambda expressions

# Keywords recognized by the language
KEYWORDS = [
    'Defun',    # Used to define a function
    'Lambd',    # Used to create a lambda expression
    'or',       # Logical OR
    'and',      # Logical AND
    'not'       # Logical NOT
]

# Characters recognized in identifiers (variable names, function names)
DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_DIGITS = LETTERS + DIGITS

# Token class to represent individual tokens in the source code
class Token:
    def __init__(self, type_, value=None):
        self.type = type_  # Type of the token (e.g., TT_INT, TT_PLUS)
        self.value = value  # Optional value of the token (e.g., the integer value for TT_INT)

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
