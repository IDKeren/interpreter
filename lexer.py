from tokens import *
from position import Position
from error import *

class Lexer:
    def __init__(self, text):
        self.text = text  # The full source code text to be tokenized
        self.pos = Position(-1, 0, -1, text)  # Initialize the position in the text
        self.current_char = None  # The current character being processed
        self.advance()  # Advance to the first character

    def advance(self):
        # Move to the next character in the input text
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def tokenize(self):
        # Tokenizes the entire source text into a list of tokens
        tokens = []

        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()  # Skip whitespace
            elif self.current_char == '#':  # Handle comments
                self.skip_comment()
            elif self.current_char.isdigit():
                tokens.append(self.make_number())
            elif self.current_char.isalpha() or self.current_char == "'":
                tokens.append(self.make_identifier())
            elif self.current_char in "+-*/%(){}==!=><&|!,":
                tokens.append(self.make_operator())
            elif self.current_char == '.':  # Handle dot (.)
                tokens.append(Token(TT_DOT))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                raise IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens

    def skip_comment(self):
        # Skips over comments in the input
        while self.current_char is not None and self.current_char != '\n':
            self.advance()
        self.advance()

    def make_number(self):
        # Handles number literals, including integers and floats
        num_str = ''
        dot_count = 0

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

    def make_identifier(self):
        id_str = ''
        while self.current_char is not None and self.current_char in LETTERS_DIGITS + '_':
            id_str += self.current_char
            self.advance()

        if id_str == 'True':
            return Token('Literal', True)
        elif id_str == 'False':
            return Token('Literal', False)
        elif id_str == 'or':
            return Token(TT_OR, id_str)
        elif id_str == 'and':
            return Token(TT_AND, id_str)
        elif id_str in KEYWORDS:
            return Token(TT_KEYWORD, id_str)
        else:
            return Token(TT_IDENTIFIER, id_str)

    def make_operator(self):
        # Handles operators and special characters
        if self.current_char == '&' and self.text[self.pos.idx + 1] == '&':
            self.advance()
            self.advance()
            return Token(TT_AND)
        elif self.current_char == '|' and self.text[self.pos.idx + 1] == '|':
            self.advance()
            self.advance()
            return Token(TT_OR)
        elif self.current_char == '+':
            self.advance()
            return Token(TT_PLUS)
        elif self.current_char == '-':
            self.advance()
            return Token(TT_MINUS)
        elif self.current_char == '*':
            self.advance()
            return Token(TT_MUL)
        elif self.current_char == '/':
            self.advance()
            return Token(TT_DIV)
        elif self.current_char == '%':  # Add this block for modulo
            self.advance()
            return Token(TT_MOD)  # Define TT_MOD in tokens.py
        elif self.current_char == '(':
            self.advance()
            return Token(TT_LPAREN)
        elif self.current_char == ')':
            self.advance()
            return Token(TT_RPAREN)
        elif self.current_char == ',':
            self.advance()
            return Token(TT_COMMA)
        elif self.current_char == '=' and self.text[self.pos.idx + 1] == '=':
            self.advance()
            self.advance()
            return Token(TT_EQ)
        elif self.current_char == '!' and self.text[self.pos.idx + 1] == '=':
            self.advance()
            self.advance()
            return Token(TT_NEQ)
        elif self.current_char == '>' and self.text[self.pos.idx + 1] == '=':
            self.advance()
            self.advance()
            return Token(TT_GTE)
        elif self.current_char == '<' and self.text[self.pos.idx + 1] == '=':
            self.advance()
            self.advance()
            return Token(TT_LTE)
        elif self.current_char == '>':
            self.advance()
            return Token(TT_GT)
        elif self.current_char == '<':
            self.advance()
            return Token(TT_LT)
        elif self.current_char == '!':
            self.advance()
            return Token(TT_NOT)
        else:
            pos_start = self.pos.copy()
            char = self.current_char
            self.advance()
            raise IllegalCharError(pos_start, self.pos, "'" + char + "'")
