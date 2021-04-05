# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

import unittest
from collections import Counter

class Solution:

    def left_rot(self, a, d):
        # good code, lets optimize it
        # extend list how much it is needed
        len_a = len(a)
        a = a * (d // len_a + 2)
        # slice it from d until d + len(a)
        return a[d: d + len_a]

        # # looks more optimized
        # res = [None] * len(a)
        # for i in (range(len(a))):
        #     if i - d >= 0: # same array
        #        res[i - d] = a[i]
        #     else:
        #        res[(i-d) % len(a)] = a[i]
        # return res





# test

#
s = Solution()

test_cases = [[[1,2,3,4,5],4000000]]

for t1 in test_cases:
    print(t1, s.left_rot(t1[0], t1[1]))


# class TestInt(unittest.TestCase):
#
#     def test_integer(self):
#         s = Solution()
#
#         test_cases = [[[1,2,3,4,5], 4]]
#         test_results = [[5,1,2,3,4]]
#
#         for i, test_case in enumerate(test_cases):
#             self.assertEqual(s.left_rot(test_case[0], test_case[1]), test_results[i])
#
#
# if __name__ == '__main__':
#     unittest.main()