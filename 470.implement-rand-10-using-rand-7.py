#
# @lc app=leetcode id=470 lang=python3
#
# [470] Implement Rand10() Using Rand7()
#
# https://leetcode.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (45.05%)
# Likes:    199
# Dislikes: 76
# Total Accepted:    9.9K
# Total Submissions: 21.9K
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
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        row, col, idx = 0, 0, 0
        while idx >= 40:
            row = rand7(); col = rand7()
            idx = 7 * (row-1) + (col-1)

        return 1 + idx % 10

        """
        i = 7
        while i > 6:
            i = rand7()

        j = 6
        while j > 5:
            j = rand7()

        if i % 2 == 0:
            return j
        else:
            return j + 5
        """

        """
        a = rand7(); b = rand7()
        idx = b + (a-1) * 7
        if idx <= 40:
            return 1 + (idx-1) % 10
        a = idx - 40
        b = rand7()
        idx = b + (a-1) * 7
        if idx <= 60:
            return 1 + (idx-1) % 60
        a = idx - 60
        b = rand7()
        idx = b + (a-1) * 7
        if idx <= 20:
            return 1 + (idx-1) % 10
        """
        

