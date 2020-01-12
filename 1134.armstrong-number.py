#
# @lc app=leetcode id=1134 lang=python3
#
# [1134] Armstrong Number
#
# https://leetcode.com/problems/armstrong-number/description/
#
# algorithms
# Easy (78.70%)
# Likes:    17
# Dislikes: 3
# Total Accepted:    5.2K
# Total Submissions: 6.6K
# Testcase Example:  '153'
#
# The k-digit number N is an Armstrong number if and only if the k-th power of
# each digit sums to N.
# 
# Given a positive integer N, return true if and only if it is an Armstrong
# number.
# 
# 
# 
# Example 1:
# 
# 
# Input: 153
# Output: true
# Explanation: 
# 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
# 
# 
# Example 2:
# 
# 
# Input: 123
# Output: false
# Explanation: 
# 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^8
# 
# 
#

# @lc code=start
class Solution:
    def isArmstrong(self, N: int) -> bool:
        return N == sum([pow(ord(a) - ord('0'), len(str(N))) for a in str(N)])
        
# @lc code=end

