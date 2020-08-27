#
# @lc app=leetcode id=470 lang=python3
#
# [470] Implement Rand10() Using Rand7()
#
# https://leetcode.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (46.30%)
# Likes:    444
# Dislikes: 138
# Total Accepted:    23.8K
# Total Submissions: 51.4K
# Testcase Example:  '1'
#
# Given a function rand7 which generates a uniform random integer in the range
# 1 to 7, write a function rand10 which generates a uniform random integer in
# the range 1 to 10.
# 
# Do NOT use system's Math.random().
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: [7]
# 
# 
# 
# Example 2:
# 
# 
# Input: 2
# Output: [8,4]
# 
# 
# 
# Example 3:
# 
# 
# Input: 3
# Output: [8,1,10]
# 
# 
# 
# 
# Note:
# 
# 
# rand7 is predefined.
# Each testcase has one argument: n, the number of times that rand10 is
# called.
# 
# 
# 
# 
# Follow up:
# 
# 
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
# 
# 
# 
# 
# 
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        row, col, idx = 0, 0, 100
        while idx > 40:
            row, col = rand7(), rand7()
            idx = col + (row - 1) * 7
        return 1 + (idx - 1) % 10
        
# @lc code=end

