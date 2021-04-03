# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen


import unittest
from collections import Counter

class Solution:

    def jumping_on_clouds(self, c):

        clouds = list(map(int, c.split()))
        # happy path
        # if sum(clouds[::2]) == 0:
        #     return len(clouds[::2]) - 1
        # else:
        steps = 0
        pos = 0
        while pos < len(clouds) - 1:
            if pos == len(clouds) - 2:
                steps += 1
                break
            if clouds[pos + 2] == 1:
                pos += 1
            else:
                pos += 2
            steps += 1
        return steps




# test

s = Solution()

# test_cases = ['0 1 0 0 0 1 0','0 0 1 0 0 1 0', '0 0 0 1 0 0']
#
# for t1 in test_cases:
#     print(t1, s.jumping_on_clouds(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = ['0 1 0 0 0 1 0','0 0 1 0 0 1 0']
        test_results = [3, 4]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.jumping_on_clouds(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
