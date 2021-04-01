import timeit

def fibonacci(n):
    a = 0
    b = 1
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
    # Check is n is equal
    # to 0
    elif n == 0:
        return
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


starttime = timeit.default_timer()
print("The start time is :", starttime)
# print(factorial(5))
print(fibonacci(999))
print("The time difference is :", timeit.default_timer() - starttime)