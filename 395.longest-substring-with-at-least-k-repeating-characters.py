#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (38.72%)
# Likes:    746
# Dislikes: 70
# Total Accepted:    48.7K
# Total Submissions: 125.5K
# Testcase Example:  '"aaabb"\n3'
#
# 
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
# 
# 
# Example 1:
# 
# Input:
# s = "aaabb", k = 3
# 
# Output:
# 3
# 
# The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# 
# 
# Example 2:
# 
# Input:
# s = "ababbc", k = 2
# 
# Output:
# 5
# 
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
# 
# 
#
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

        

