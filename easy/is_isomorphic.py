# https://leetcode.com/problems/isomorphic-strings/

import unittest
import string

class Solution:

    def is_isomorphic(self, str1, str2):
        # checks
        if not len(str1) == len(str2) \
                or any([x for x in list(str1) if x not in string.ascii_letters]) \
                or any([x for x in list(str2) if x not in string.ascii_letters]):
            return False

        hmap = {}

        for i in range(0, len(str1)):
            if str1[i] not in hmap:
                if str2[i] in hmap.values():
                    return False
                else:
                    hmap[str1[i]] = str2[i]
            else:
                if hmap[str1[i]] != str2[i]:
                    return False
            # if str1[i] not in hmap:
            #     if str2[i] in hmap.values():
            #         return False
            #     else:
            #         hmap[str1[i]] = str2[i]
            # else:
            #     if hmap[str1[i]] != str2[i]:
            #         return False
        return True


# test


# s = Solution()
#
# test_cases = [["egg", "add"],["foo", "bar"],["paper", "title"]]
# for t1, t2 in test_cases:
#     print(t1, t2, s.roman_to_integer(t1,t2))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [["egg", "add"],["foo", "bar"],["paper", "title"]]
        test_results = [True, False, True]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.is_isomorphic(test_case[0], test_case[1]), test_results[i])


if __name__ == '__main__':
    unittest.main()
