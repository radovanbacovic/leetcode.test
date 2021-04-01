# https://leetcode.com/problems/contains-duplicate/


import unittest
from collections import Counter

class Solution:
    # 1/3 with Counter
    # def contains_duplicate(self, nums):
    #     c = Counter(nums)
    #     for v in c.values():
    #         if v > 1:
    #             return True
    #     return False

    # 2/3 sets
    # def contains_duplicate(self, nums):
    #     if len(set(nums)) != len(nums):
    #         return True
    #     return False

    # 3/3 native coding style
    def contains_duplicate(self, nums):
        temp = []
        for i in nums:
            if i in temp:
                return True
            temp.append(i)
        return False


# test

s = Solution()

# test_cases = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
#
# for t1 in test_cases:
#     print(t1, s.contains_duplicate(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
        test_results = [True, False, True]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.contains_duplicate(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
