#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (44.30%)
# Likes:    547
# Dislikes: 48
# Total Accepted:    32.8K
# Total Submissions: 73.9K
# Testcase Example:  '"ABAB"\n2'
#
# Given a string that consists of only uppercase English letters, you can
# replace any letter in the string with another letter at most k times. Find
# the length of a longest substring containing all repeating letters you can
# get after performing the above operations.
# 
# Note:
# Both the string's length and k will not exceed 10^4.
# 
# 
# 
# Example 1:
# 
# Input:
# s = "ABAB", k = 2
# 
# Output:
# 4
# 
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "AABABBA", k = 1
# 
# Output:
# 4
# 
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# 
#
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = defaultdict(int)
        maxn = i = j = 0
        for i, v in enumerate(s, 1):
            count[v] += 1
            maxn = max(maxn, count[v])
            if i - j - maxn > k:
                count[s[j]] -= 1
                j += 1
        return i - j
        

