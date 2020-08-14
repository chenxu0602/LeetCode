#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (43.92%)
# Likes:    423
# Dislikes: 148
# Total Accepted:    100.4K
# Total Submissions: 228.6K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
from itertools import zip_longest
from functools import reduce

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # O(max(N1, N2))

        # z = zip_longest(num1[::-1], num2[::-1], fillvalue='0')
        # res, carry, zero2 = [], 0, 2 * ord('0')
        # for i in z:
        #     cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
        #     carry, r = divmod(cur_sum, 10)
        #     res.append(str(r))
        # return ('1' if carry else '') + ''.join(res[::-1])


        return str(
            reduce(lambda a, b: 10 * a + b,
                map(lambda x: ord(x[0]) + ord(x[1]) - 2 * ord('0'),
                    list(zip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
                )
            )
        )




        

