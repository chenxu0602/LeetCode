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

        def isPalindrom(s):
            return s == s[::-1]

        def dfs(s, L):
            if not s:
                res.append(L)
            for i in range(1, len(s)+1):
                if isPalindrom(s[:i]):
                    dfs(s[i:], L+[s[:i]])

        res = []
        dfs(s, [])
        return res
        
# @lc code=end

