# https://leetcode.com/problems/two-sum/
import unittest

class Solution:

    def two_sum(self, nums, target):
        temp_dict = {}
        for i, num in enumerate(nums):
            if target - num not in temp_dict:
                temp_dict[num] = i
            else:
                return [temp_dict[target - num], i]

# test

# s = Solution()
# test_cases = [[[2, 7, 11, 15], 9], [[3, 2, 4], 6],[[3, 3], 6]]
# for n, t in test_cases:
#     print(n, t, ' === ', s.two_sum(n, t))



class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[[2, 7, 11, 15], 9], [[3, 2, 4], 6],[[3, 3], 6]]
        test_results = [[0, 1], [1, 2], [0, 1]]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.two_sum(test_case[0], test_case[1]), test_results[i])


if __name__ == '__main__':
    unittest.main()
