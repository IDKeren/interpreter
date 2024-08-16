prime_descending = lambda lst: sorted([x for x in lst if x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))], reverse=True)

result = prime_descending([29, 15, 7, 18, 5, 20, 13, 23, 4])
print(result)
