# https://leetcode.com/problems/remove-duplicates-from-sorted-array/



import unittest


class Solution:

    def remove_dups(self, nums):
        i = 0
        for j in range(len(nums) - 1):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i


# test

s = Solution()

test_cases = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]

for t1 in test_cases:
    print(t1, s.remove_dups(t1))


# class TestInt(unittest.TestCase):
#
#     def test_integer(self):
#         s = Solution()
#
#         test_cases = [[1,1,2], [0,0,1,1,1,2,2,3,3,4]]
#         test_results = [2, 5]
#
#         for i, test_case in enumerate(test_cases):
#             self.assertEqual(s.contains_duplicate(test_case), test_results[i])
#
#
# if __name__ == '__main__':
#     unittest.main()
