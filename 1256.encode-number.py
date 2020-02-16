#
# @lc app=leetcode id=1256 lang=python3
#
# [1256] Encode Number
#
# https://leetcode.com/problems/encode-number/description/
#
# algorithms
# Medium (63.90%)
# Likes:    22
# Dislikes: 74
# Total Accepted:    2.8K
# Total Submissions: 4.4K
# Testcase Example:  '23'
#
# Given a non-negative integer num, Return its encoding string.
# 
# The encoding is done by converting the integer to a string using a secret
# function that you should deduce from the following table:
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: num = 23
# Output: "1000"
# 
# 
# Example 2:
# 
# 
# Input: num = 107
# Output: "101100"
# 
# 
# 
# Constraints:
# 
# 
# 0 <= num <= 10^9
# 
#

# @lc code=start
class Solution:
    def encode(self, num: int) -> str:
        return bin(num+1)[3:]
        
# @lc code=end

