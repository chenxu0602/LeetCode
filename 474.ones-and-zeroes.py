#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (39.91%)
# Likes:    578
# Dislikes: 138
# Total Accepted:    32.2K
# Total Submissions: 80.7K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# In the computer world, use restricted resource you have to generate maximum
# benefit is what we always want to pursue.
# 
# For now, suppose you are a dominator of m 0s and n 1s respectively. On the
# other hand, there is an array with strings consisting of only 0s and 1s.
# 
# Now your task is to find the maximum number of strings that you can form with
# given m 0s and n 1s. Each 0 and 1 can be used at most once.
# 
# Note:
# 
# 
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4
# 
# Explanation: This are totally 4 strings can be formed by the using of 5 0s
# and 3 1s, which are “10,”0001”,”1”,”0”
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2
# 
# Explanation: You could form "10", but then you'd have nothing left. Better
# form "0" and "1".
# 
# 
# 
# 
#
class Solution:
    def countzeroesones(self, s):
        c = [0, 0]
        for i, v in enumerate(s):
            c[ord(str(v)) - ord('0')] += 1
        return c

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            count = self.countzeroesones(s)
            for zeroes in range(m, count[0]-1, -1):
                for ones in range(n, count[1]-1, -1):
                    dp[zeroes][ones] = max(1 + dp[zeroes-count[0]][ones-count[1]], dp[zeroes][ones])

        return dp[m][n]

        

