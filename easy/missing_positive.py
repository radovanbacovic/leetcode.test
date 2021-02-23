# https://leetcode.com/problems/first-missing-positive/


import unittest


class Solution:

    def missing_positive(self, input_list):
        # remove negatives and 0
        working_list = list(filter(lambda x: x > 0, input_list))

        for w in range(1, len(working_list) + 2):
            if not w in working_list:
                return w

        return -1
# test


# s = Solution()
#
# test_cases = [[1,2,0], [3,4,-1,1], [7,8,9,11,12]]
#
# for t1 in test_cases:
#     print(t1, s.roman_to_integer(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12]]
        test_results = [3, 2, 1]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.missing_positive(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
