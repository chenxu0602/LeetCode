#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (45.23%)
# Likes:    741
# Dislikes: 20
# Total Accepted:    33.6K
# Total Submissions: 74.3K
# Testcase Example:  '"sea"\n"eat"'
#
# 
# Given two words word1 and word2, find the minimum number of steps required to
# make word1 and word2 the same, where in each step you can delete one
# character in either string.
# 
# 
# Example 1:
# 
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
# 
# 
# 
# Note:
# 
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.
# 
# 
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Using Longest Common Subsequence- Dynamic Programming
        # lcs[i][j] represents the length of the longest common subsequence among s1 and s2 upto (i-1)th and (j-1)th index.
        # Time  complexity: O(mn)
        # Space complexity: O(mn)
        l1, l2 = map(len, (word1, word2))
        lcs = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

        return l1 + l2 - 2 * lcs[l1][l2]


        # Without using LCS Dynamic Programmming 
        # Time  complexity: O(mn)
        # Space complexity: O(mn)
        # l1, l2 = map(len, (word1, word2))
        # dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        # for i in range(l1 + 1):
        #     for j in range(l2 + 1):
        #         if i == 0 or j == 0:
        #             dp[i][j] = i + j
        #         elif word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        # return dp[l1][l2]


        # 1-D Dynamic Programming
        # Time  complexity: O(mn)
        # Space complexity: O(n)
        # l1, l2 = map(len, (word1, word2))
        # dp = [0] * (l2 + 1)
        # for i in range(l1 + 1):
        #     temp = [0] * (l2 + 1)
        #     for j in range(l2 + 1):
        #         if i == 0 or j == 0:
        #             temp[j] = i + j
        #         elif word1[i - 1] == word2[j - 1]:
        #             temp[j] = dp[j - 1]
        #         else:
        #             temp[j] = 1 + min(dp[j], temp[j - 1])
        #     dp = temp

        # return dp[l2]
        

