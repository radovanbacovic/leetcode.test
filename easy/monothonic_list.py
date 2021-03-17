import unittest


class Solution:

    def monothonic_list(self, input_list):
       return input_list == sorted(input_list) or \
              input_list == sorted(input_list, reverse=True)

# test

# s = Solution()
# test_cases = [[1, 7, 8, 20], [10, 7, 4, 2], [1, 5, 4, 10, 11], [10, 9, 11]]
# for t in test_cases:
#     print(t, s.two_sum(t))
#


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[1, 7, 8, 20], [10, 7, 4, 2], [1, 5, 4, 10, 11], [10, 9, 11]]
        test_results = [True, True, False, False]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.monothonic_list(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
