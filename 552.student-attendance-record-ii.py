#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#
# https://leetcode.com/problems/student-attendance-record-ii/description/
#
# algorithms
# Hard (33.55%)
# Likes:    298
# Dislikes: 60
# Total Accepted:    13.4K
# Total Submissions: 39.8K
# Testcase Example:  '1'
#
# Given a positive integer n, return the number of all possible attendance
# records with length n, which will be regarded as rewardable. The answer may
# be very large, return it after mod 10^9 + 7.
# 
# A student attendance record is a string that only contains the following
# three characters:
# 
# 
# 
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
# 
# 
# 
# 
# A record is regarded as rewardable if it doesn't contain more than one 'A'
# (absent) or more than two continuous 'L' (late).
# 
# Example 1:
# 
# Input: n = 2
# Output: 8 
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent
# times. 
# 
# 
# 
# Note:
# The value of n won't exceed 100,000.
# 
# 
# 
# 
#
class Solution:
    def checkRecord(self, n: int) -> int:
        # O(n)
        M = 1000000007

        f = [0] * 6
        if n > 5:
            f = [0] * (n + 1)

        f[0] = 1
        f[1] = 2
        f[2] = 4
        f[3] = 7

        # The P and L cases
        for i in range(4, n+1):
            f[i] = ((2 * f[i-1]) % M + (M - f[i-4])) % M
        
        # The A case
        sums = f[n]
        for i in range(1, n+1):
            sums += (f[i-1] * f[n-i]) % M

        return sums % M

        
        

