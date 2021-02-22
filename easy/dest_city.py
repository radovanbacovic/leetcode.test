# https://leetcode.com/problems/destination-city/

import unittest

class Solution:

    def dest_city(self, input_list):
        src = set([s[0] for s in input_list])
        dest = set([d[1] for d in input_list])

        return (dest - src).pop()


# test
#
# s = Solution()
# test_cases = [[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]]
# for t in test_cases:
#     print(t, s.dest_city(t))



class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]],
                      [["B", "C"], ["D", "B"], ["C", "A"]],
                      [["A","Z"]]]
        test_results = ["Sao Paulo", "A", "Z"]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.dest_city(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
