#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (44.20%)
# Likes:    536
# Dislikes: 42
# Total Accepted:    24.2K
# Total Submissions: 54.5K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
# 
# 
# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
# 
# 
# Note:
# 
# 
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
# 
# 
#
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        waiting = defaultdict(list)

        """
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        """

        for it in map(iter, words):
            waiting[next(it)].append(it)

        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)

        return len(waiting[None])

        

