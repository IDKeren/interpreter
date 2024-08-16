from functools import reduce

concatenate = lambda strings: reduce(lambda x, y: x + ' ' + y, strings)

result = concatenate(["Hello", "world"])
print(result)
