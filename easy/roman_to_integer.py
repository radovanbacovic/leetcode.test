# https://leetcode.com/problems/roman-to-integer/


import unittest


class Solution:

    def roman_to_integer(self, input_string):
        basic_nums = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}

        spec_nums = {'IV': 4,
                     'IX': 9,
                     'XL': 40,
                     'XC': 90,
                     'CD': 400,
                     'CM': 900}
        res = []

        for k, v in spec_nums.items():
            if k in input_string:
                input_string = input_string.replace(k, '')
                res.append(v)

        res.extend([basic_nums[i] for i in input_string])

        return sum(res)

        #
        # basic_list = []
        #
        # for b in basic_list:
        #     res.append(basic_nums[b])
        #
        # return sum(res)
# test

# s = Solution()
#
# test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV", "MCMXCIII"]
#
# for t1 in test_cases:
#     print(t1, s.roman_to_integer(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV", "MCMXCIII"]
        test_results = [3, 4, 9, 58, 1994, 1993]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.roman_to_integer(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
