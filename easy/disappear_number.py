# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

import unittest
from collections import Counter

class Solution:

    def disppear_number(self, input_list):
        full_list = set([x for x in range(1, len(input_list) + 1)])

        return list(full_list.difference(input_list))
# test
#
# s = Solution()
# test_cases = [[4, 3, 2, 7, 8, 2, 3, 1]]
# for t in test_cases:
#     print(t, s.dest_city(t))



class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[4, 3, 2, 7, 8, 2, 3, 1]]
        test_results = [[5, 6]]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.disppear_number(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()

