#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (27.92%)
# Likes:    1228
# Dislikes: 277
# Total Accepted:    179.6K
# Total Submissions: 629.8K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        """
        dp = [[""] for _ in range(len(s)+1)]

        for i in range(1, len(s)+1):
            lst = []
            for j in range(i):
                if len(dp[j]) > 0 and s[j:i] in wordDict:
                    for l in dp[j]:
                        new_elem = l + " " + s[j:i]
                        lst.append(new_elem.strip())
            dp[i] = lst
        return dp[-1]
        """

        def check(s, wd):
            ok = [True]
            for i in range(1, len(s)+1):
                ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
            return ok[-1]

        def dfs(s, wd, L):
            if check(s, wd):
                if len(s) == 0:
                    res.append(L[1:])
                for i in range(1, len(s)+1):
                    if s[:i] in wd:
                        dfs(s[i:], wd, L+' '+s[:i])

        res = []
        dfs(s, wordDict, "")
        return res

    
            
        
# @lc code=end

