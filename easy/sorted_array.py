# https://leetcode.com/problems/squares-of-a-sorted-array/


import unittest

class Solution:

    def sorted_array(self, nums):
        return sorted([n **2 for n in nums])

# test

#
# s = Solution()
# test_cases = [[-4,-1,0,3,10], [-7,-3,2,3,11], [1]]
# for t in test_cases:
#     print(t, s.happy_number(t))
#


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[-4,-1,0,3,10], [-7,-3,2,3,11], [1]]
        test_results = [[0,1,9,16,100], [4,9,9,49,121], [1]]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.sorted_array(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
