#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
#
# algorithms
# Easy (59.34%)
# Likes:    127
# Dislikes: 8
# Total Accepted:    13.4K
# Total Submissions: 22.6K
# Testcase Example:  '"aa"'
#
# Given a string s, return the length of the longest substring between two
# equal characters, excluding the two characters. If there is no such substring
# return -1.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# 
# Example 1:
# 
# 
# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two
# 'a's.
# 
# Example 2:
# 
# 
# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# 
# 
# Example 3:
# 
# 
# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
# 
# 
# Example 4:
# 
# 
# Input: s = "cabbac"
# Output: 4
# Explanation: The optimal substring here is "abba". Other non-optimal
# substrings include "bb" and "".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 300
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        positions = defaultdict(list)

        for i, c in enumerate(s):
            positions[c].append(i)

        res = -1
        for c in positions:
            if len(positions[c]) > 1:
                res = max(res, positions[c][-1] - positions[c][0] - 1)

        return res
        
# @lc code=end

