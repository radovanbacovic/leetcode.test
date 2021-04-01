"""
Write a function that returns the elements on odd positions (0 based) in a list
"""


def solution(input):
    # code goes here
    output = [x for x in input if x % 2 == 1]
    return output



assert solution([0, 1, 2, 3, 4, 5]) == [1, 3, 5], 'x'
assert solution([1, -1, 2, -2]) == [-1, -2], 'x'
