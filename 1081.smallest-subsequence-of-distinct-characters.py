#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (43.27%)
# Likes:    179
# Dislikes: 34
# Total Accepted:    5.1K
# Total Submissions: 11.6K
# Testcase Example:  '"cdadabcc"'
#
# Return the lexicographically smallest subsequence of text that contains all
# the distinct characters of text exactly once.
# 
# 
# 
# Example 1:
# 
# 
# Input: "cdadabcc"
# Output: "adbc"
# 
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: "abcd"
# 
# 
# 
# Example 3:
# 
# 
# Input: "ecbacba"
# Output: "eacb"
# 
# 
# 
# Example 4:
# 
# 
# Input: "leetcode"
# Output: "letcod"
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= text.length <= 1000
# text consists of lowercase English letters.
# 
# 
# 
# 
# 
# 
#
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = {c: i for i, c in enumerate(text)}
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)

        

