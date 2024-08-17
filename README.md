**Functional Programming Language Interpreter**
Welcome to the Functional Programming Language Interpreter! 
This interpreter allows you to define functions, use lambda expressions, and perform various computations in a custom functional programming language.

**Features:**
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
git clone https://github.com/IDKeren/interpreter.git
cd interpreter

Ensure you have Python 3.x installed:
python3 --version

Run the REPL:
python3 main.py

**Usage**
Once the interpreter is running, you can start entering expressions or full programs directly into the REPL.

Method 1: Line-By-Line String Input

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

Method 2: Multi-Line String Input

Example 5: Recursive Function
>>> Defun factorial(n)
 ((n == 0) or (n * factorial(n - 1)))
 factorial(5)
120

Example 6: Multi Functions
Defun factorial(n) 
((n == 0) or (n * factorial(n - 1))) 
Defun fibonacci(n)
((n == 1) or (fibonacci(n - 1) + fibonacci(n - 2)))
Defun is_even(n)
  ((n % 2) == 0)
factorial(5)
fibonacci(10)
is_even(4)

Output:
120
89
True

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

**Design Decisions, Challenges Faced, and Solutions Implemented**

Introduction
The goal of this project was to design and implement a functional programming language interpreter capable of handling fundamental features like lambda expressions, recursion, and basic arithmetic and boolean operations. The interpreter was intended to support both interactive use via a Read-Eval-Print Loop (REPL) and the execution of complete programs. Throughout the project, several design decisions were made to meet these goals, and various challenges were encountered and addressed.

Design Decisions
Language Features
The language was designed to support key functional programming features, including:

Function Definitions: To enable function creation and function application.
Lambda Expressions: To enable anonymous function creation and higher-order functions.
Recursion: To allow functions to call themselves, a critical feature for many functional algorithms.
Basic Data Types: Including integers and booleans, with support for arithmetic and boolean operations.
These features were chosen to provide a foundation for exploring functional programming concepts while keeping the language simple enough to implement within the project's scope.

Lexical Analysis
A custom lexer was implemented to tokenize the input source code. The design focused on:

Handling Whitespace and Comments: Ignoring spaces and comments to focus on meaningful tokens.
Recognizing Keywords, Identifiers, and Operators: Ensuring that keywords like Defun and Lambd, as well as operators (+, -, *, etc.), were correctly identified.
This lexer was crucial for translating source code into a sequence of tokens that the parser could then process.

Parsing Strategy
The parser was designed using a recursive descent approach, which allowed for a straightforward implementation of the language's grammar. Key decisions included:

Function Definitions: Parsing function definitions with the Defun keyword, ensuring that function names, arguments, and bodies were correctly associated.
Expression Handling: Supporting complex expressions, including nested operations and boolean logic, through a series of parsing functions (e.g., expression(), term(), factor()).
This approach allowed for clear, modular parsing functions that could be debugged and extended as needed.

Environment Handling
The interpreter uses a global environment to store variable and function definitions. 
This decision was made to simplify scope management, particularly within the REPL, where persistence across commands is desirable. 

**The environment supports:**
Function and Variable Definitions: 
Ensuring that once a function or variable is defined, it remains accessible across different inputs.
Recursion Handling: Allowing functions to call themselves by ensuring they remain in the environment during execution.
This design facilitated ease of use within the REPL while accommodating the functional programming paradigm's needs.

**Error Handling**
Comprehensive error handling was implemented to ensure the interpreter could gracefully handle incorrect input. 

The design focused on:
Syntax Errors: Providing meaningful feedback when the parser encounters unexpected tokens or incomplete expressions.
Runtime Errors: Detecting and reporting issues like undefined variables or functions during evaluation.
This robust error handling was critical for maintaining a smooth user experience within the REPL.

**Challenges Faced**
Parsing Complex Expressions
One of the significant challenges was correctly parsing complex expressions, particularly when they involved nested operations or multi-line input. 
The initial parser implementation struggled with handling lambda expressions and function bodies, leading to errors or incomplete parsing.

Multi-line Input Handling in REPL
Handling multi-line input in the REPL was another challenge, especially when users pasted multiple lines at once. The REPL needed to correctly determine when an input was complete before attempting to process it. Initially, this led to issues where the REPL would prematurely attempt to evaluate incomplete input, resulting in errors.

Recursion and Scope Management
Managing recursion within a global environment presented challenges, particularly when ensuring that functions could correctly call themselves without losing track of their environment. This required careful handling of function definitions and argument passing.

Error Recovery
Ensuring the REPL could recover from errors without crashing or requiring a restart was a crucial challenge. Initially, errors in the input could leave the REPL in an inconsistent state, making it difficult for users to continue without resetting the interpreter.

Implement Lambd expression(Partial solution)
The interpreter creates a lambda object that stores the environment where it was created, its parameter, and its body. When applied, it substitutes the argument into the lambda's body and evaluates it.

**Solutions Implemented:**
Multi-line Input Handling
To address the challenges with multi-line input, the REPL was modified to detect when an input was likely incomplete and switch to a continuation prompt (...). This approach allowed users to enter functions and complex expressions over multiple lines without confusing the REPL.

Parser Enhancements
The parser was enhanced to better handle the transition between different parts of a function definition, such as moving from the parameter list to the function body. Improvements were also made to ensure that nested expressions were correctly parsed and evaluated.

Environment Management
The environment was designed to persist across inputs in the REPL, allowing for the correct handling of recursive functions and variable scope. This included ensuring that function definitions remained accessible throughout the program's execution and that recursion was handled without introducing scope issues.

Improved Error Reporting
The interpreter's error handling was enhanced to provide clearer, more actionable feedback when users encountered syntax or runtime errors. This included catching errors in a way that allowed the REPL to clear its buffer and reset its state, enabling users to continue without interruption.

Conclusion
The design decisions and solutions implemented in this project resulted in a functional interpreter capable of handling key functional programming concepts. The challenges faced, particularly around parsing and multi-line input handling, were met with targeted improvements to the REPL and parser. Future improvements could focus on adding more advanced language features and refining the environment management to support more complex scoping rules.
