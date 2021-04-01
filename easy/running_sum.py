# https://leetcode.com/problems/running-sum-of-1d-array/


import unittest


class Solution:

    def running_sum(self, nums):
        # res = []
        # for i in range(len(nums)):
        #     res.append(sum(nums[:i+1]))
        # return res

        return [sum(nums[:i+1]) for i in range(len(nums))]

# test

s = Solution()

# test_cases = [[1,2,3,4], [1,1,1,1,1], [3,1,2,10,1]]
#
# for t1 in test_cases:
#     print(t1, s.contains_duplicate(t1))
#

class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[1,2,3,4], [1,1,1,1,1], [3,1,2,10,1]]
        test_results = [[1,3,6,10], [1,2,3,4,5], [3,4,6,16,17]]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.running_sum(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
