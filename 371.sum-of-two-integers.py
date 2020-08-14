#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (50.70%)
# Likes:    1288
# Dislikes: 2279
# Total Accepted:    192.3K
# Total Submissions: 379.3K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # O(1)
        # x, y = abs(a), abs(b)
        # # ensure x >= y
        # if x < y:
        #     return self.getSum(b, a)  
        # sign = 1 if a > 0 else -1
        
        # if a * b >= 0:
        #     # sum of two positive integers
        #     while y:
        #         x, y = x ^ y, (x & y) << 1
        # else:
        #     # difference of two positive integers
        #     while y:
        #         x, y = x ^ y, ((~x) & y) << 1
        
        # return x * sign


        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        max_int = 0x7FFFFFFF  # To manage the overflow
        return a if a < max_int else ~(a ^ mask)
        
# @lc code=end

