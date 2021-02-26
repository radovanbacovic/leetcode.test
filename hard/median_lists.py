# https://leetcode.com/problems/median-of-two-sorted-arrays/


import unittest
import statistics

class Solution:

    def median_lists(self, nums1, nums2):
        return statistics.median(sorted(nums1 + nums2))
# test


# s = Solution()
#
# test_cases = [[[1, 3], [2]], [[1, 2], [3, 4]], [[0, 0], [0, 0]], [[], [1]], [[2], []]]
#
# for t1, t2 in test_cases:
#     print(t1, t2, s.median_lists(t1, t2))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[[1, 3], [2]], [[1, 2], [3, 4]], [[0, 0], [0, 0]], [[], [1]], [[2], []]]
        test_results = [2, 2.5, 0, 1, 2]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.median_lists(test_case[0], test_case[1]), test_results[i])


if __name__ == '__main__':
    unittest.main()
