from lexer import Lexer
from myParser import Parser
from interpreter import Interpreter


def repl():
    print("Welcome to the functional programming language REPL. Type 'exit' to quit.")
    buffer = ""
    global_env = {}  # Persistent environment across inputs
    while True:
        try:
            line = input('>>> ')
            if line.strip().lower() == 'exit':
                break

            buffer += line + "\n"

            lexer = Lexer(buffer)
            tokens = lexer.tokenize()
            parser = Parser(tokens)

            try:
                ast = parser.parse()
                interpreter = Interpreter(ast, env=global_env)  # Pass the global environment
                result = interpreter.evaluate()
                if result is not None:
                    print(result)
                buffer = ""  # Clear the buffer after successful execution
            except SyntaxError:
                # If a SyntaxError occurs, continue to accept more input lines
                continue
            except Exception as e:
                print(f"Error: {e}")
                buffer = ""  # Clear the buffer on error
        except Exception as e:
            print(f"Error: {e}")
            buffer = ""  # Clear the buffer on error


if __name__ == '__main__':
    repl()


