# https://leetcode.com/problems/robot-return-to-origin/

import unittest
from collections import Counter

class Solution:

    def single_num(self, nums):
        counter = Counter(nums)
        for k,v in counter.items():
            if v == 1:
                return k
        return -1

# test

# s = Solution()
# test_cases = [[2,2,1],[4,1,2,1,2], [1]]
# for t in test_cases:
#     print(t, s.single_num(t))



class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[2,2,1],[4,1,2,1,2], [1]]
        test_results = [1, 4, 1]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.single_num(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
