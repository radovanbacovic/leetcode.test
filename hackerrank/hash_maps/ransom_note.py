# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

import unittest
from collections import Counter

class Solution:

    def ransom_note(self, magazine, note):
        magazine_counter = Counter(magazine)
        note_counter = Counter(note)

        for k, v in note_counter.items():
            if k in magazine_counter:
                if magazine_counter[k] < v:
                    return 'No'
            else:
                return 'No'
        return 'Yes'


# test

s = Solution()

# test_cases = [['give me one grand today night','give one grand today'],
#               ['two times three is not four','two times two is four'],
#               ['ive got a lovely bunch of coconuts','ive got some coconuts'],
#               ['attack at dawn','Attack at dawn']]
#
# test_cases = [[x.rstrip().split(), y.rstrip().split()] for x,y in test_cases]
#
# for t1 in test_cases:
#      print(t1, s.count_triplets(t1[0], t1[1]))


class TestInt(unittest.TestCase):

    def test_integer(self):
        s = Solution()

        test_cases = [['give me one grand today night','give one grand today'],
                      ['two times three is not four','two times two is four'],
                      ['ive got a lovely bunch of coconuts','ive got some coconuts'],
                      ['attack at dawn','Attack at dawn']]
        test_results = ['Yes', 'No', 'No','No']

        for i, test_case in enumerate(test_cases):
            self.assertEqual(s.ransom_note(test_case[0], test_case[1]), test_results[i])


if __name__ == '__main__':
    unittest.main()
