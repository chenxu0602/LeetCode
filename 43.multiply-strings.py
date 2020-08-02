#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (32.54%)
# Likes:    1429
# Dislikes: 658
# Total Accepted:    254.9K
# Total Submissions: 783K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
from functools import reduce 

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # m, n = len(num1), len(num2)
        # pos = [0] * (m + n)

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        #         idx_1, idx_2 = i + j, i + j + 1
        #         mul += pos[idx_2]

        #         pos[idx_1] += mul // 10
        #         pos[idx_2] = mul % 10

        # k = 0
        # for l in range(len(pos)):
        #     if pos[l] > 0:
        #         k = l
        #         break

        # return str(int(reduce(lambda a, b: str(a) + str(b), pos[k:])))

        m, n = len(num1), len(num2)
        pos = [0] * (m + n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                idx_1, idx_2 = i + j, i + j + 1
                mul += pos[idx_2]

                pos[idx_1] += mul // 10
                pos[idx_2] = mul % 10

        k = 0
        for l in range(len(pos)):
            if pos[l] > 0:
                k = l
                break

        return str(int(reduce(lambda a, b: str(a) + str(b), pos[k:])))
        
# @lc code=end

