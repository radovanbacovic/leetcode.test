# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

import unittest
from collections import Counter
class Solution:
    # base loop
    # find min member of array to start
    # then: count min * n
    # then again count min * n *n (to get triplets)

    # will go in opposite direction
    def count_triplets(self, arr, r):
        # too slow
        # res = 0
        # for max_member in [x for x in arr if x >= 1 * r * r]:
        #     mid_member = arr.count(max_member / r)
        #     min_member = arr.count(max_member / r / r)
        #     res += mid_member * min_member
        # return res

        triplet_dict = {}

        # still do not cover edge cases
        # for max_member in [x for x in arr if x >= 1 * r * r]:
        #     mid_member = int(max_member / r)
        #     min_member = int(mid_member / r)
        #     if (max_member, mid_member, min_member) in triplet_dict:
        #         triplet_dict[(max_member, mid_member, min_member)] += arr.count(mid_member) * arr.count(min_member)
        #     else:
        #         triplet_dict[(max_member, mid_member, min_member)] = arr.count(mid_member) * arr.count(min_member)
        # print(triplet_dict)
        # return sum(triplet_dict.values())

        count = 0
        dict = {}
        dict_pairs = {}

        # shit is working
        # for max_member in reversed(arr):
        #     if max_member * r in dict_pairs:
        #         count += dict_pairs[max_member * r]
        #     if max_member * r in dict:
        #         dict_pairs[max_member] = dict_pairs.get(max_member, 0) + dict[max_member * r]
        #
        #     dict[max_member] = dict.get(max_member, 0) + 1
        # return count

        for max_member in reversed(arr):
            if max_member * r in dict_pairs:
                count += dict_pairs[max_member * r]
            if max_member * r in dict:
                dict_pairs[max_member] = dict_pairs.get(max_member, 0) + dict[max_member * r]

            dict[max_member] = dict.get(max_member, 0) + 1
        return count

# test

s = Solution()
#
# test_cases = [[[1,3,9,9,27,81],3]] #[[[1,2,2,4],2], [[1,3,9,9,27,81],3], [[1, 5, 5, 25, 125],5]]
#
# for t1 in test_cases:
#     print(t1, s.count_triplets(t1[0], t1[1]))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [[[1,2,2,4],2], [[1,3,9,9,27,81],3], [[1, 5, 5, 25, 125],5]]
        test_results = [2,6,4]

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.count_triplets(test_case[0], test_case[1]), test_results[i])


if __name__ == '__main__':
    unittest.main()