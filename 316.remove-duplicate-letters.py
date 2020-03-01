#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (34.20%)
# Likes:    1059
# Dislikes: 94
# Total Accepted:    69.4K
# Total Submissions: 202.4K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appears once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# Example 1:
# 
# 
# Input: "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: "cbacdcbc"
# Output: "acdb"
# 
# 
# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # result = ""
        # while s:
        #     i = min(map(s.rindex, set(s)))
        #     c = min(s[:i+1])
        #     result += c
        #     s = s[s.index(c):].replace(c, "")
        # return result

        rindex = {c: i for i, c in enumerate(s)}
        result = ""
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result
        
# @lc code=end

