#
# @lc app=leetcode id=522 lang=python3
#
# [522] Longest Uncommon Subsequence II
#
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/
#
# algorithms
# Medium (32.98%)
# Likes:    109
# Dislikes: 489
# Total Accepted:    17.3K
# Total Submissions: 52.5K
# Testcase Example:  '["aba","cdc","eae"]'
#
# 
# Given a list of strings, you need to find the longest uncommon subsequence
# among them. The longest uncommon subsequence is defined as the longest
# subsequence of one of these strings and this subsequence should not be any
# subsequence of the other strings.
# 
# 
# 
# A subsequence is a sequence that can be derived from one sequence by deleting
# some characters without changing the order of the remaining elements.
# Trivially, any string is a subsequence of itself and an empty string is a
# subsequence of any string.
# 
# 
# 
# The input will be a list of strings, and the output needs to be the length of
# the longest uncommon subsequence. If the longest uncommon subsequence doesn't
# exist, return -1.
# 
# 
# Example 1:
# 
# Input: "aba", "cdc", "eae"
# Output: 3
# 
# 
# 
# Note:
# 
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].
# 
# 
#
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def subseq(w1, w2):
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return i == len(w1)

        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            if all(not subseq(word1, word2) for j, word2 in enumerate(strs) if j != i):
                return len(word1)

        return -1


        

