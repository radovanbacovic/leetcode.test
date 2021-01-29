#  https://leetcode.com/problems/factorial-trailing-zeroes/
import unittest
import math

class Solution:
    def trailing_zeroes(self, x):
        return math.factorial(x)

# test
s = Solution()
print(s.trailing_zeroes(5))

# class TestInt(unittest.TestCase):
#
#     def test_integer(self):
#         s = Solution()
#
#         test_cases = [123, -456, 0, 567, -1]
#         test_results = [321, -654, 0, 765, -1]
#
#         for i, test_case in enumerate(test_cases):
#             self.assertEqual(s.trailing_zeroes(test_case), test_results[i])
#
#
# if __name__ == '__main__':
#     unittest.main()