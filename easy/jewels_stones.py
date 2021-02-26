# https://leetcode.com/problems/jewels-and-stones/

import unittest

from collections import Counter

class Solution:

    def jewels_stones(self, jewels, stones):
        cnt = Counter(x for x in stones if x in jewels)
        res = 0
        for j in list(jewels):
            res += cnt.get(j,0)

        return res
# test

# s = Solution()
#
# test_cases = [["aA", "aAAbbbb"], ["z", "ZZ"]]
#
# for t1, t2 in test_cases:
#     print(t1, t2, s.jewels_stones(t1, t2))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [["aA", "aAAbbbb"], ["z", "ZZ"]]
        test_results = [3, 0]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.jewels_stones(test_case[0], test_case[1]), test_results[i])


if __name__ == '__main__':
    unittest.main()
