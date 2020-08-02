#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (38.10%)
# Likes:    1310
# Dislikes: 55
# Total Accepted:    138.3K
# Total Submissions: 362.3K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
# 
# It's guaranteed the answer fits on a 32-bit signed integer.
# 
# Example 1:
# 
# 
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 
# 
# Example 2:
# 
# 
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
# 
# 
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # Iterative Dynamic Programming
        # Time/Space complexity: O(M x N)
        # M, N = map(len, (s, t))
        # dp = [[0] * (N + 1) for _ in range(M + 1)]

        # for j in range(N + 1):
        #     dp[M][j] = 0

        # for i in range(M + 1):
        #     dp[i][N] = 1

        # for i in range(M - 1, -1, -1):
        #     for j in range(N - 1, -1, -1):
        #         dp[i][j] = dp[i + 1][j]

        #         if s[i] == t[j]:
        #             dp[i][j] += dp[i + 1][j + 1]

        # return dp[0][0]


        # Space optimized Dynamic Programming
        # Time  complexity: O(M x N)
        # Space complexity: O(N)
        M, N = map(len, (s, t))
        dp = [0] * N

        for i in range(M - 1, -1, -1):
            prev = 1
            for j in range(N - 1, -1, -1):
                old_dpj = dp[j]

                if s[i] == t[j]:
                    dp[j] += prev

                prev = old_dpj

        return dp[0]

        
# @lc code=end

