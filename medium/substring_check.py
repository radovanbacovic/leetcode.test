# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/


import unittest


class Solution:

    def substring_check(self, s, t):
        return None

# test

s = Solution()

test_cases = [['a','a'], ['abe', 'bbc'], ['ab', 'bb'], ['aba', 'baba']]

for t1, t2 in test_cases:
    print(t1, s.substring_check(t1, t2))


# class TestInt(unittest.TestCase):
#
#     def test_integer(self):
#         s = Solution()
#
#         test_cases = [['a','a'], ['abe', 'bbc'], ['ab', 'bb'], ['aba', 'baba']]
#         test_results = [0, 10, 3, 6]
#
#         for i, test_case in enumerate(test_cases):
#             self.assertEqual(s.substring_check(test_case), test_results[i])
#
#
# if __name__ == '__main__':
#     unittest.main()
