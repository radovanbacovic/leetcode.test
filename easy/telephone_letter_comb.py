# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import unittest

from itertools import product

class Solution:
    num_to_letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                      '8': 'tuv', '9': 'wxyz'}


    def telephone_letter_comb(self, nums):
            if len(nums) == 0:
                return []
            else:
                return [''.join(s) for s in product(*[self.num_to_letters[i] for i in nums])]


# test

s = Solution()

# test_cases = ["23", "", "2"]
# for t in test_cases:
#     print(t, s.telephone_letter_comb(t))
#


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = ["23", "", "2"]
        test_results = [["ad","ae","af","bd","be","bf","cd","ce","cf"], [], ["a","b","c"]]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.telephone_letter_comb(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
