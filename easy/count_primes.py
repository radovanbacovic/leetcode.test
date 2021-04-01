# https://leetcode.com/problems/count-primes/


import unittest


class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True


    def count_primes(self, num):
        res = 0
        for i in range(2, num + 1):
            if self.is_prime(i):
                res += 1
        return res


# test

s = Solution()

# test_cases = [10, 0, 1, 13]
#
# for t1 in test_cases:
#     print(t1, s.contains_duplicate(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [10, 0, 1]
        test_results = [4, 0, 0]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.count_primes(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
