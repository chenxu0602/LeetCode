#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/
#
# algorithms
# Medium (60.43%)
# Likes:    62
# Dislikes: 2
# Total Accepted:    4.5K
# Total Submissions: 7.5K
# Testcase Example:  '12'
#
# Given an integer n, return true if it is possible to represent n as the sum
# of distinct powers of three. Otherwise, return false.
# 
# An integer y is a power of three if there exists an integer x such that y ==
# 3^x.
# 
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: true
# Explanation: 12 = 3^1 + 3^2
# 
# 
# Example 2:
# 
# 
# Input: n = 91
# Output: true
# Explanation: 91 = 3^0 + 3^2 + 3^4
# 
# 
# Example 3:
# 
# 
# Input: n = 21
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^7
# 
# 
#

# @lc code=start
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        while n:
            if n % 3 == 2:
                return False
            
            n //= 3

        return True
        
        
# @lc code=end

