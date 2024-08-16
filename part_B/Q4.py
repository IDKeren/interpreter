def cumulative_operation(operation):
    def apply_operation(sequence):
        result = sequence[0]
        for item in sequence[1:]:
            result = operation(result, item)
        return result
    return apply_operation

factorial = cumulative_operation(lambda x, y: x * y)

def factorial_of(n):
    return factorial(range(1, n + 1))

print(factorial_of(5)) 

exponentiation = cumulative_operation(lambda x, y: x * y)

def power(base, exponent):
    return exponentiation([base] * exponent)

print(power(2, 3)) 

