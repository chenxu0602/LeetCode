#
# @lc app=leetcode id=1118 lang=python3
#
# [1118] Number of Days in a Month
#
# https://leetcode.com/problems/number-of-days-in-a-month/description/
#
# algorithms
# Easy (56.91%)
# Likes:    8
# Dislikes: 52
# Total Accepted:    2.5K
# Total Submissions: 4.5K
# Testcase Example:  '1992\n7'
#
# Given a year Y and a month M, return how many days there are in that
# month.
# 
# 
# 
# Example 1:
# 
# 
# Input: Y = 1992, M = 7
# Output: 31
# 
# 
# Example 2:
# 
# 
# Input: Y = 2000, M = 2
# Output: 29
# 
# 
# Example 3:
# 
# 
# Input: Y = 1900, M = 2
# Output: 28
# 
# 
# 
# 
# Note:
# 
# 
# 1583 <= Y <= 2100
# 1 <= M <= 12
# 
# 
#

# @lc code=start
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:

        days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }


        if not M == 2:
            return days[M]

        leap = False

        if Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0):
            leap = True


        if leap:
            return 29

        return days[M]
            
        

        
# @lc code=end

