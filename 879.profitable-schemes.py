#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#
# https://leetcode.com/problems/profitable-schemes/description/
#
# algorithms
# Hard (39.65%)
# Likes:    236
# Dislikes: 29
# Total Accepted:    9.8K
# Total Submissions: 24.7K
# Testcase Example:  '5\n3\n[2,2]\n[2,3]'
#
# There is a group of G members, and a list of various crimes they could
# commit.
# 
# The i^th crime generates a profit[i] and requires group[i] members to
# participate in it.
# 
# If a member participates in one crime, that member can't participate in
# another crime.
# 
# Let's call a profitable scheme any subset of these crimes that generates at
# least P profit, and the total number of members participating in that subset
# of crimes is at most G.
# 
# How many schemes can be chosen?  Since the answer may be very large, return
# it modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: G = 5, P = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation: 
# To make a profit of at least 3, the group could either commit crimes 0 and 1,
# or just crime 1.
# In total, there are 2 schemes.
# 
# 
# 
# Example 2:
# 
# 
# Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
# Output: 7
# Explanation: 
# To make a profit of at least 5, the group could commit any crimes, as long as
# they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and
# (0,1,2).
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= G <= 100
# 0 <= P <= 100
# 1 <= group[i] <= 100
# 0 <= profit[i] <= 100
# 1 <= group.length = profit.length <= 100
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        # Dynamic Programming
        # Time  complexity: O(N x P x G), where N is the number of crimes available to the gang.
        # Space complexity: O(P x G)
        # MOD = 10**9 + 7
        # cur = [[0] * (G + 1) for _ in range(P + 1)]
        # cur[0][0] = 1

        # for p0, g0 in zip(profit, group):
        #     cur2 = [row[:] for row in cur]
        #     for p1 in range(P + 1):
        #         p2 = min(p1 + p0, P)
        #         for g1 in range(G - g0 + 1):
        #             g2 = g1 + g0
        #             cur2[p2][g2] += cur[p1][g1]
        #             cur2[p2][g2] %= MOD
        #     cur = cur2

        # return sum(cur[-1]) % MOD


        MOD = 10**9 + 7
        dp = [[0] * (G + 1) for _ in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(P, i + p)][g + j] += dp[i][j]

        return sum(dp[P]) % MOD
        
# @lc code=end

