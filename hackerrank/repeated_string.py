# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


import unittest


class Solution:

    def repeated_string(self, s, n):
        return s.count('a') * (n // len(s)) + s[: n % len(s)].count('a')
        # overflow error
        # return list(filter(lambda x: x == 'a', list(s * (n // len(s) + 1))[:n])).count('a')
# test

s = Solution()

# test_cases = [('abcac', 10), ('aba', 10),('a', 1000000000000)]
#
# for t1, t2 in test_cases:
#     print(t1, s.repeated_string(t1, t2))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [('abcac', 10),
                      ('aba', 10),
                      ('a', 1000000000000)]
        test_results = [4, 7, 1000000000000]

        for i,k in enumerate(test_cases):
            self.assertEqual(s.repeated_string(k[0], k[1]), test_results[i])


if __name__ == '__main__':
    unittest.main()
