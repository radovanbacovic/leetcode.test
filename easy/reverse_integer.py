#  https://leetcode.com/problems/reverse-integer/
import unittest


class Solution:
    def reverse(self, x):
        res = int(''.join([i for i in str(abs(x))][::-1]))

        if x == 0:
            return 0
        elif x > 0:
            return res
        else:
            return -res

# test


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [123, -456, 0, 567, -1]
        test_results = [321, -654, 0, 765, -1]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.reverse(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()