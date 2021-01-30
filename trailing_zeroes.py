#  https://leetcode.com/problems/factorial-trailing-zeroes/
import unittest
import math


class Solution:
    def trailing_zeroes(self, x):
        res: int = 0
        fact = list(str(math.factorial(x)))[::-1]

        for f in fact:
            if f == '0':
                res += 1
            else:
                return res
        return res

# test


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [3, 5, 0, 10]
        test_results = [0, 1, 0, 2]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.trailing_zeroes(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
