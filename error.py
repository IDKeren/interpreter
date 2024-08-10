# error.py
# This file defines the error handling classes used by the lexer and parser.

class Error(Exception):
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start  # Start position of the error
        self.pos_end = pos_end      # End position of the error
        self.error_name = error_name  # Name of the error (e.g., "Illegal Character")
        self.details = details      # Details about the error

    def as_string(self):
        # Return a string representation of the error
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.text}, line {self.pos_start.ln + 1}'
        return result

# Specific error for illegal characters
class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)
