"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def iterative_str_len(a_str):
    result = 0
    for i in range(len(a_str)):
        result += 1
    return result



def recursive_str_len(a_str):
    if len(a_str) == 0:
        return 0
    else:
        return recursive_str_len(a_str[1:]) + 1


input_str = "I love recursion"
print(len(input_str))  # Standard Pythonic way
print(iterative_str_len(input_str))
print(recursive_str_len(input_str))