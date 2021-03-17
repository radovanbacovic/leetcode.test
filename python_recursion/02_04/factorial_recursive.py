def factorial(n):
    #  n = 5  res: 5 * 4 * 3 * 2 * 1
    if n <= 1:
        # base case
        return 1
    else:
        # resursive case
        return n * factorial(n - 1)



print(factorial(4))
print(factorial(6))
print(factorial(1))
print(factorial(0))
print(factorial(-7))
