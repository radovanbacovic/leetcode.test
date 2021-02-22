# https://leetcode.com/problems/happy-number/



import unittest

class Solution:
    def happy_number(self, input_number):
        D = {input_number,}
        while True:
            input_number = sum(int(x)**2 for x in str(input_number))
            if input_number == 1:
                return True
            if input_number in D:
                return False
            D.add(input_number)






# test


s = Solution()
test_cases = [19, 2]
for t in test_cases:
    print(t, s.happy_number(t))


#
# class TestInt(unittest.TestCase):
#
#     def test_integer(self):
#         s = Solution()
#
#         test_cases = [19, 2]
#         test_results = [True, False]
#
#         for i, test_case in enumerate(test_cases):
#             self.assertEqual(s.happy_number(test_case), test_results[i])
#
#
# if __name__ == '__main__':
#     unittest.main()
