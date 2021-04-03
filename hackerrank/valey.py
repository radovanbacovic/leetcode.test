# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen


import unittest
from collections import Counter

class Solution:
    ### SLOW!
    # def valey(self, path):
    #     num_path = [0] + [-1 if x == 'D' else 1 for x in list(path)]
    #     running_pos = []
    #     res = 0
    #     for n in range(len(num_path)):
    #         current_pos = sum(num_path[0:n+1])
    #         if n > 0 and current_pos == 0 and running_pos[n-1] < 0:
    #             res += 1
    #         running_pos.append(current_pos)
    #
    #     return res

    # this one is great
    def valey(self, path):
        num_path = [0] + [-1 if x == 'D' else 1 for x in list(path)]
        running_pos = 0
        res = 0
        for n in range(len(num_path)):
            running_pos += num_path[n]

            if n > 0 and running_pos == 0 and running_pos - num_path[n] < 0:
                res += 1
        return res
# test

# s = Solution()
#
# test_cases = ['DDUUUUDD', 'UDDDUDUU']
#
# for t1 in test_cases:
#     print(t1, s.valey(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = ['UDDDUDUU', 'DDUUUUDD']
        test_results = [1, 1]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.valey(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
