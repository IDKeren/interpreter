'''Answer to Q7:

Eager Evaluation: All values are generated and stored in memory before any processing takes place.
This can consume more memory and possibly more computation upfront.

Lazy Evaluation: Values are generated and processed on the fly, only when needed.
This can be more efficient, especially when not all values need to be generated, or when working with large data sets.

In this specific example, the output remains the same for both cases,
but the process by which the results are obtained is different, showcasing the concept of lazy evaluation in the second case '''

def generate_values():
 print('Generating values...')
 yield 1
 yield 2
 yield 3

def square(x):
 print(f'Squaring {x}')
 return x * x

print('Eager evaluation:')
values = list(generate_values())
squared_values = [square(x) for x in values]
print(squared_values)
print('\nLazy evaluation:')
squared_values = [square(x) for x in generate_values()]
print(squared_values)

