#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
# https://leetcode.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (60.77%)
# Likes:    78
# Dislikes: 16
# Total Accepted:    15.3K
# Total Submissions: 26.1K
# Testcase Example:  '4'
#
# The Tribonacci sequence Tn is defined as follows: 
# 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# 
# Given n, return the value of Tn.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# 
# 
# Example 2:
# 
# 
# Input: n = 25
# Output: 1389537
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 -
# 1.
# 
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:

        """
        memo = [0, 1, 1]
        if n < 2:
            return memo[n]
        for i in range(2, n):
            memo.append(memo[-1] + memo[-2] + memo[-3])
        return memo[-1]
        """

        if n < 3:
            return 1 if n else 0

        x, y, z = 0, 1, 1
        for _ in range(n-2):
            x, y, z = y, z, x + y + z
        return z



# @lc code=end

