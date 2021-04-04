# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

import unittest

class Solution:
    # collect all possibilities list x 2
    # try to find intersect s1 and s2 - if yes we have good result
    def two_strings(self, s1, s2):
        # slow option
        # comb_s1 = set(s1[x:y] for y in range(len(s1) + 1) for x in range(len(s1)) if y > x and y-x <= len(s2))
        # comb_s2 = set(s2[x:y] for y in range(len(s2) + 1) for x in range(len(s2)) if y > x and y-x <= len(s1))
        #
        # return 'NO' if len(list(comb_s1 & comb_s2)) <= 0 else 'YES'

        # Still slow
        # comb_s1 = set(s1[x:y] for y in range(len(s1) + 1) for x in range(len(s1)) if y > x and y - x <= len(s2))
        # for x in range(len(s2)):
        #     for y in range(1, len(s2)+1):
        #         if s2[x:y] in comb_s1:
        #             return 'YES'
        # return 'NO'

        # one line winner
        return 'YES' if set(s1) & set(s2) else 'NO'
# test

s = Solution()

# test_cases = [['and', 'art'], ['be', 'cat'], ['hello', 'world'], ['hi', 'world']]
#
# for t1 in test_cases:
#      print(t1, s.count_triplets(t1[0], t1[1]))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [['and', 'art'], ['be', 'cat'], ['hello', 'world'], ['hi', 'world']]
        test_results = ['YES', 'NO', 'YES','NO']

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.two_strings(test_case[0], test_case[1]), test_results[i])


if __name__ == '__main__':
    unittest.main()