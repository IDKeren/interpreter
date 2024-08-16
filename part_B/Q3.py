from functools import reduce

def cumulative_sum_of_squares_even(numbers):
    return list(map(
        lambda sublist: reduce(
            lambda acc, x: acc + (lambda y: y ** 2)(x),
            filter(
                lambda num: (lambda z: z % 2 == 0)(num),
                sublist
            ),
            0
        ),
        numbers
    ))

input_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = cumulative_sum_of_squares_even(input_list)
print(result) 
