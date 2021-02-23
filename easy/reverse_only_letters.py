# https://leetcode.com/problems/reverse-only-letters/


import unittest
import string


class Solution:

    def reverse_only_letters(self, input_string):
        """
        :type input_string: str
        """

        # Checks
        if input_string in ['\\', '"'] or \
                len(input_string) > 100 or \
                len([x for x in list(input_string) if 33 > ord(x) or ord(x) > 122]) > 0:
            return None

        res = []
        let_only = [let for let in input_string if let.isalpha()]

        for letter in input_string:
            if letter.isalpha():
                res.append(let_only.pop())
            else:
                res.append(letter)
        return ''.join(res)


# test

# s = Solution()
# test_cases = ["ab-cd", "a-bC-dEf-ghIj", "Test1ng-Leet=code-Q!"]
# for t in test_cases:
#     print(t, s.integer_to_roman(t))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = ["ab-cd", "a-bC-dEf-ghIj", "Test1ng-Leet=code-Q!"]
        test_results = ["dc-ba", "j-Ih-gfE-dCba", "Qedo1ct-eeLg=ntse-T!"]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.reverse_only_letters(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
