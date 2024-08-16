from functools import reduce

count_palindromes = lambda lst: list(map(lambda sublist: reduce(lambda count, s: count + 1, filter(lambda s: s == s[::-1], sublist), 0), lst))

input_lists = [
    ["aba", "hello", "ima"],
    ["banana", "apple"],
]

result = count_palindromes(input_lists)
print(result) 
