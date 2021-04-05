# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import unittest

class Solution:

    def ny_chaos(self, q):
        # bribe_dict = {}
        # list_sorted = sorted(q)
        # my_list = q.copy()

        # for i in range(len(q) - 1):
        #
        #     if my_list[i] == list_sorted[i]: # this is correct place
        #         pass
        #     else: # switch values
        #         bribe_dict[my_list[i]] = bribe_dict.get(my_list[i], 0) + 1
        #         temp = my_list[i + 1]
        #         my_list[i+1] = my_list[i]
        #         my_list[i] = temp
        #         print('   ', my_list)
        #         print(bribe_dict)
        #     if my_list == list_sorted:
        #
        #         print('Too chaotic' if max(bribe_dict.values()) >= 3 else sum(bribe_dict.values()))

            bribes = 0
            for i in range(len(q) - 1, -1, -1):
                if q[i] - (i + 1) > 2:
                    print('Too chaotic')
                    return
                for j in range(max(0, q[i] - 2), i):
                    if q[j] > q[i]:
                        bribes += 1
            print(bribes)






# test

s = Solution()

# test_cases = [[1,2,5,3,4,7,8,6],[1,2,3,5,4,6,7,8], [4,1,2,3], [2, 1, 5, 3, 4]]
#
# for t1 in test_cases:
#     print(t1, s.left_rot(t1))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[1,2,5,3,4,7,8,6],[1,2,3,5,4,6,7,8], [4,1,2,3], [2, 1, 5, 3, 4]]
        test_results = ['Too chaotic', 1, 'Too chaotic', 'Too chaotic']

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.ny_chaos(test_case), test_results[i])


if __name__ == '__main__':
    unittest.main()