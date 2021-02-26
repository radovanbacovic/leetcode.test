# https://leetcode.com/problems/integer-to-roman/

import unittest


class Solution:

    def integer_to_roman(self, input_num):
        basic_nums = {1: 'I',
                      5: 'V',
                      10: 'X',
                      50: 'L',
                      100: 'C',
                      500: 'D',
                      1000: 'M'}

        spec_nums = {4: 'IV',
                     9: 'IX',
                     40: 'XL',
                     90: 'XC',
                     400: 'CD',
                     900: 'CM'}

        res_str = []
        num_list = [int(x) for x in str(input_num)][::-1]

        for i in range(len(num_list)):
            # give me number like 1000, 100, 10 ...
            temp_res = num_list[i] * 10**i
            # check special numbers
            if temp_res in spec_nums.keys():
                res_str.append(spec_nums[temp_res])
            # check base numbers
            elif temp_res in basic_nums.keys():
                res_str.append(basic_nums[temp_res])
            else:
                # check basic numbers <> [1, 5, 9]
                my_num = divmod(num_list[i], 5)
                res_str.extend([my_num[1] * basic_nums[1], my_num[0] * basic_nums[5]])

        return ''.join(res_str[::-1])

# test

# s = Solution()
#
# test_cases = [3, 4, 9, 58, 1994, 1996]
#
# for t1 in test_cases:
#     print(t1, s.jewels_stones(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [3, 4, 9, 58, 1994, 1993, 1]
        test_results = ["III", "IV", "IX", "LVIII", "MCMXCIV", "MCMXCIII", "I"]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.integer_to_roman(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
