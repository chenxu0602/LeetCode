#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#
# https://leetcode.com/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (48.27%)
# Likes:    184
# Dislikes: 6
# Total Accepted:    5K
# Total Submissions: 10.1K
# Testcase Example:  '"abac"\n"cab"'
#
# Given two strings str1 and str2, return the shortest string that has both
# str1 and str2 as subsequences.  If multiple answers exist, you may return any
# of them.
# 
# (A string S is a subsequence of string T if deleting some number of
# characters from T (possibly 0, and the characters are chosen anywhere from T)
# results in the string S.)
# 
# 
# 
# Example 1:
# 
# 
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a subsequence of "cabac" because we can delete the first
# "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these
# properties.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
# 
# 
#
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        """
        m, n = len(str1), len(str2)
        dp = [list(range(n+1))] + [[i] + [0]*n for i in range(1, m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = 1 + (dp[i][j] if str1[i] == str2[j] else min(dp[i+1][j], dp[i][j+1]))

        i, j, scs = m, n, ""
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                scs += str1[i-1]
                i, j = i-1, j-1
            elif dp[i-1][j] > dp[i][j-1]:
                scs += str2[j-1]
                j -= 1
            else:
                scs += str1[i-1]
                i -= 1
        return str1[:i] + str2[:j] + scs
        """

        def lcs(A, B):
            m, n = len(A), len(B)
            dp = [["" for _ in range(n+1)] for _ in range(m+1)]
            for i in range(m):
                for j in range(n):
                    if A[i] == B[j]:
                        dp[i+1][j+1] = dp[i][j] + A[i]
                    else:
                        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key=len)
            return dp[-1][-1]

        res, i, j = "", 0, 0
        for c in lcs(str1, str2):
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        return res + str1[i:] + str2[j:]

        

