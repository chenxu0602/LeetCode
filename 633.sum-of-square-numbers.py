#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.65%)
# Likes:    355
# Dislikes: 238
# Total Accepted:    48K
# Total Submissions: 146.9K
# Testcase Example:  '5'
#
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a^2 + b^2 = c.
# 
# Example 1:
# 
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: False
# 
# 
# 
# 
#
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        all, idx = set(), 0

        while idx * idx <= c:
            all.add(idx * idx)
            idx += 1

        for v in all:
            if c - v in all:
                return True

        return False
        

