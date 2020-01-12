#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.53%)
# Likes:    564
# Dislikes: 812
# Total Accepted:    174.5K
# Total Submissions: 463.7K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:

        """
        r = 0
        while n > 0:
            n //= 5
            r += n
        return r
        """

        if n < 5:
            return 0

        if n < 10:
            return 1

        return n // 5 + self.trailingZeroes(n//5)
        
# @lc code=end

