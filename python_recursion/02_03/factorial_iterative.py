def factorial_iterative_while(n):
    #  n = 5  res: 5 * 4 * 3 * 2 * 1
    result = 1

    while n >= 1:
        result *= n
        n -= 1
    return result



assert factorial_iterative_while(4) == 24
assert factorial_iterative_while(6) == 720
assert factorial_iterative_while(1) == 1
assert factorial_iterative_while(0) == 1
assert factorial_iterative_while(-7) == 1
