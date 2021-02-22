
import unittest


class Solution:

    def recuring_string(self, input_str):
        already_there = []
        for i in input_str:
            if i in already_there:
                return i
            else:
                already_there.append(i)
        return None
# test

# s = Solution()
# test_cases = ['AABA', 'ABCCA', 'A', 'CBALKL']
# for t in test_cases:
#     print(t, s.missing_num(t))

#

class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = ['AABA', 'ABCCA', 'A', 'CBALKL']
        test_results = ['A', 'C', None, 'L']

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.recuring_string(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
