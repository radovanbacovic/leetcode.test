# https://leetcode.com/problems/robot-return-to-origin/

import unittest


class Solution:

    def robot_origin(self, moves):
        # x = 0
        # y = 0

        # for move in list(moves):
        #     if move == 'L':
        #         x -= 1
        #     elif move == 'R':
        #         x += 1
        #     elif move == 'D':
        #         y -= 1
        #     elif move == 'U':
        #         y += 1
        #
        # return x == y == 0
        if not moves:
            return True
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

# test

# s = Solution()
# test_cases = [98711, 12322] #, 1234, 123456789, 0, 12322]
# for t in test_cases:
#     print(t, s.roman_to_integer(t))
#


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = ['UD', 'LL', 'RRDD', 'LDRRLRUULR']
        test_results = [True, False, False, False]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.robot_origin(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()
