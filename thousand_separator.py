# https://leetcode.com/problems/thousand-separator/

import unittest


class Solution:

    def thousand_separator(self, x):
        if x == 0:
            return '0'
        else:
            res = []
            my_list = list(str(x))[::-1]
            for i, num in enumerate(my_list):
                if i % 3 == 0 and i > 0:
                    res.append('.')
                res.append(num)
            return ''.join(res[::-1])
# test

# s = Solution()
# test_cases = [98711, 12322] #, 1234, 123456789, 0, 12322]
# for t in test_cases:
#     print(t, s.thousand_separator(t))
#

class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [987, 1234, 123456789, 0, 12322]
        test_results = ['987', '1.234', '123.456.789', '0', '12.322']

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.thousand_separator(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
