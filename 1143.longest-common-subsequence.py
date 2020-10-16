#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (58.38%)
# Likes:    2031
# Dislikes: 25
# Total Accepted:    145.8K
# Total Submissions: 249.5K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order
# of the remaining characters. (eg, "ace" is a subsequence of "abcde" while
# "aec" is not). A common subsequence of two strings is a subsequence that is
# common to both strings.
# 
# 
# 
# If there is no common subsequence, return 0.
# 
# 
# Example 1:
# 
# 
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# 
# 
# Example 3:
# 
# 
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time  complexity: O(M x N)
        # Space complexity: O(M x N)
        # @lru_cache(None)
        # def memo_solve(p1, p2):
        #     # Base case: If either string is now empty, we can't match
        #     # up anymore characters.
        #     if p1 == len(text1) or p2 == len(text2):
        #         return 0

        #     # Recursive case 1.
        #     if text1[p1] == text2[p2]:
        #         return 1 + memo_solve(p1 + 1, p2 + 1)
        #     # Recursive case 2.
        #     else:
        #         return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))

        # return memo_solve(0, 0)
        

        # Time  complexity: O(M x N)
        # Space complexity: O(M x N)
        # m, n = map(len, (text1, text2))
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(m):
        #     for j in range(n):
        #         dp[i + 1][j + 1] = 1 + dp[i][j] if text1[i] == text2[j] else max(dp[i + 1][j], dp[i][j + 1])
        # return dp[-1][-1]


        # Time  complexity: O(M x N)
        # Space complexity: O(min(M, N))
        # if len(text2) < len(text1):
        #     text1, text2 = text2, text1

        # # The previous column starts with all 0's and like before is 1
        # # more than the length of the first word.
        # previous = [0] * (len(text1) + 1)

        # # Iterate up each column
        # for col in range(len(text2)):
        #     # Create a new array to represent the current column.
        #     current = [0] * (len(text1) + 1)
        #     for row in range(len(text1)):
        #         if text2[col] == text1[row]:
        #             current[row + 1] = 1 + previous[row]
        #         else:
        #             current[row + 1] = max(previous[row + 1], current[row])
        #     previous = current

        # return previous[-1]


        # Time  complexity: O(M x N)
        # Space complexity: O(min(M, N))
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        # The previous and current column starts with all 0's and like 
        # before is 1 more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)

        for col in range(len(text2)):
            for row in range(len(text1)):
                if text2[col] == text1[row]:
                    current[row + 1] = 1 + previous[row]
                else:
                    current[row + 1] = max(previous[row + 1], current[row])
            previous, current = current, previous

        return previous[-1]


# @lc code=end

