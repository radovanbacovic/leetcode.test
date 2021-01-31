# https://leetcode.com/problems/strong-password-checker/
import string
import unittest

class Solution:

    def strong_password(self, x):
        steps = 5
        # It has at least 6 characters and at most 20 characters.
        if len(x) >= 6 and len(x) < 20:
            steps -= 1
        # It contains at least one lowercase letter,
        for p in x:
            if p in string.ascii_lowercase:
                steps -= 1
                break
        # at least one uppercase letter,
        for p in x:
            if p in string.ascii_uppercase:
                steps -= 1
                break
        # and at least one digit.
        for p in x:
            if p in string.digits:
                steps -= 1
                break
        # It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong
        pass_list = list(x)
        char_val = 0
        for i in range(len(pass_list) - 2):
            if pass_list[i] == pass_list[i+1] == pass_list[i+2]:
                char_val += 1

        if char_val == 0:
            steps -= 1
        return steps
# test

# s = Solution()
# test_cases = ['a', 'aA1', '1337C0d3','Th1sIsNotStrongggPass']
# for t in test_cases:
#     print(t, s.strong_password(t))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = ['a', 'aA1', '1337C0d3','Th1sIsNotStrongggPass']
        test_results = [5, 3 ,0, 1]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.strong_password(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
