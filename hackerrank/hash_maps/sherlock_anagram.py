# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

import unittest
from collections import Counter

class Solution:

    def sherlock_anagram(self, s):
        # anagram, contains the same element in the sub/list
        # need to go through list and see all combinations len(s)-1
        # for each combination, need to find do I have it in the array
        # store combination to improve bigO

        buckets = {}
        #
        for i in range(len(s)):
            for j in range(1, len(s) - i + 1):
                key = frozenset(Counter(s[i:i+j]).items())
                buckets[key] = buckets.get(key, 0) + 1

        count = 0
        for key in buckets:
            count += buckets[key] * (buckets[key] - 1) // 2

        return count



# test


s = Solution()

# test_cases = ['mom', 'abba', 'abcd', 'ifailuhkqq', 'kkkk', 'cdcd']


# for t1 in test_cases:
#     print(t1, s.left_rot(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = ['mom','abba', 'abcd', 'ifailuhkqq','kkkk', 'cdcd']
        test_results = [2, 4, 0, 3, 10, 5]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.sherlock_anagram(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()