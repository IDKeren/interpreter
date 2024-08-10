# position.py
# This file defines the Position class used to track the position of characters in the source code.

class Position:
    def __init__(self, idx, ln, col, text):
        self.idx = idx     # Current index in the text
        self.ln = ln       # Current line number
        self.col = col     # Current column number
        self.text = text   # Full text being processed

    def advance(self, current_char=None):
        # Move the position forward by one character
        self.idx += 1
        self.col += 1

        # If the current character is a newline, move to the next line
        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        # Create a copy of the current position
        return Position(self.idx, self.ln, self.col, self.text)
