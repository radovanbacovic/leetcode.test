# https://leetcode.com/problems/long-pressed-name/

import unittest

class Solution:

    def long_pressed_name(self, name, typed):
        if name == typed:
            return True


        l_name = []

        temp = '-'
        place = -1

        # Generate LIST name
        for n in list(name):
            if n != temp:
                l_name.append([n, 1])
                place += 1
            else:
                l_name[place] = [n, l_name[place][1] + 1]
            temp = n

        # Generate LIST typed
        l_typed = []

        temp = '-'
        place = -1
        for t in list(typed):
            if t != temp:
                l_typed.append([t, 1])
                place += 1
            else:
                l_typed[place] = [t, l_typed[place][1] + 1]
            temp = t

        # Check size and if different return
        if len(l_name) != len(l_typed):
            return False
        else:
            for l in range(len(l_name) - 1):
                if l_name[l][0] != l_typed[l][0]:
                    return False
                else:
                    if l_name[l][1] > l_typed[l][1]:
                        return False
            return True

        # Loop via LISTs


# test


s = Solution()

# test_cases = [['alex','aaleex'], ['saeed','ssaaedd'],['leelee','lleeelee'], ['laiden', 'laiden']]
# test_cases = [['leelee','lleeelee']]
# for t1, t2 in test_cases:
#     print(t1, t2, s.jewels_stones(t1,t2))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [['alex','aaleex'], ['saeed','ssaaedd'],['leelee','lleeelee'], ['laiden', 'laiden']]
        test_results = [True, False, True, True]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.long_pressed_name(test_case[0], test_case[1]), test_results[i])


if __name__ == '__main__':
    unittest.main()
