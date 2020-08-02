#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (42.14%)
# Likes:    1171
# Dislikes: 48
# Total Accepted:    185.5K
# Total Submissions: 430.2K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # O(n x 2^n)
        # For a string with length n, there will be (n - 1) intervals between chars.
        # For every interval, we can cut it or not cut it, so there will be 2^(n - 1) ways to partition the string.
        # For every partition way, we need to check if it is palindrome, which is O(n).

        # def isPalindrom(s):
        #     return s == s[::-1]

        # def dfs(s, L):
        #     if not s:
        #         res.append(L)
        #     for i in range(1, len(s) + 1):
        #         if isPalindrom(s[:i]):
        #             dfs(s[i:], L + [s[:i]])

        # res = []
        # dfs(s, [])
        # return res

        dp = [[] for _ in range(len(s) + 1)]
        dp[-1] = [[]]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    for k in dp[j]:
                        dp[i].append([s[i:j]] + k)

        return dp[0]
        
# @lc code=end

