# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


import unittest
from collections import Counter

class Solution:

    def socks(self, input_socks):
        pairs = 0
        c = Counter(input_socks)
        return sum([x//2 for x in c.values()])

# test

s = Solution()

# test_cases = [[10, 20, 20, 10, 10, 30, 50, 10, 20], [1, 2, 1, 2, 1, 3, 2]]
#
# for t1 in test_cases:
#     print(t1, s.left_rot(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[10, 20, 20, 10, 10, 30, 50, 10, 20], [1, 2, 1, 2, 1, 3, 2]]
        test_results = [3, 2]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.socks(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
