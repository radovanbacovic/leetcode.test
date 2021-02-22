# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

import unittest

class Solution:

    def greatest_element(self, input_list):
        if len(input_list) == 1:
            return [-1]

        res = [-1]*len(input_list)

        for i in range(1, len(input_list)):
            res[i] = (max(input_list[i:]))

        # res.append(-1)
        return res
# test

# s = Solution()
# test_cases = [[17, 18, 5, 4, 6, 1]]
# for t in test_cases:
#     print(t, s.dest_city(t))



class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[17,18,5,4,6,1], [400]]
        test_results = [[18,6,6,6,1,-1], [-1]]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.greatest_element(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
