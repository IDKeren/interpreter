Functional Programming Language Interpreter
Welcome to the Functional Programming Language Interpreter! 
This interpreter allows you to define functions, use lambda expressions, and perform various computations in a custom functional programming language.

Features:
Arithmetic Operations: Supports addition (+), subtraction (-), multiplication (*), division (/), and modulo (%).
Boolean Operations: Supports logical operations such as AND (&&), OR (||), and NOT (!).
Comparison Operations: Supports equality (==), inequality (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).
Lambda Expressions: Supports anonymous functions defined using the Lambd keyword.
Function Definitions: Allows defining named functions using the Defun keyword.
Function Application: Supports applying functions, including higher-order functions.
Global Environment: Maintains a persistent environment across multiple REPL commands.
REPL Mode: Interactive Read-Eval-Print Loop for executing commands one line at a time.

**Getting Started**

Prerequisites:
Python 3.x is required to run this interpreter.
Ensure all necessary files (lexer.py, myParser.py, interpreter.py, tokens.py, etc.) are in the same directory.

**Installation**
Clone the repository:
git clone https://github.com/your-repo/interpreter.git
cd interpreter

Ensure you have Python 3.x installed:
python3 --version

Run the REPL:
python3 main.py

**Usage**
Once the interpreter is running, you can start entering expressions or full programs directly into the REPL.

Example 1: Basic Arithmetic
>>> 3 + 4 * 2
11
>>> (10 - 2) / 4
2

Example 2: Lambda Expressions
>>> (Lambd x. (Lambd y. (x + y)))(3)(4)
7

Example 3: Function Definition
>>> Defun add(a, b) (a + b)
>>> add(5, 6)
11

Example 4: Recursive Function
>>> Defun factorial(n) ((n == 0) or (n * factorial(n - 1)))
>>> factorial(5)
120

**Exiting the REPL**
Type exit: To exit the REPL, simply type exit and press Enter.
Use Ctrl+C or Ctrl+D: You can also exit using keyboard shortcuts.

**Persistent Environment**
The environment (i.e., variables and function definitions) persists across REPL commands. 
You can define a function in one command and use it in subsequent commands.

>>> Defun square(x) (x * x)
>>> square(4)
16
>>> square(9)
81
