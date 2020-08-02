#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (40.10%)
# Likes:    1188
# Dislikes: 223
# Total Accepted:    348.2K
# Total Submissions: 851.4K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # if len(a) == 0:
        #     return b
        # if len(b) == 0:
        #     return a

        # if a[-1] == '1' and b[-1] == '1':
        #     return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'

        # if a[-1] == '0' and b[-1] == '0':
        #     return self.addBinary(a[0:-1], b[0:-1]) + '0'
        # else:
        #     return self.addBinary(a[0:-1], b[0:-1]) + '1'

        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

        
        
# @lc code=end

