#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#
# https://leetcode.com/problems/group-shifted-strings/description/
#
# algorithms
# Medium (49.57%)
# Likes:    315
# Dislikes: 54
# Total Accepted:    54.6K
# Total Submissions: 108.6K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the
# sequence:
# 
# 
# "abc" -> "bcd" -> ... -> "xyz"
# 
# Given a list of strings which contains only lowercase alphabets, group all
# strings that belong to the same shifting sequence.
# 
# Example:
# 
# 
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
# ⁠ ["abc","bcd","xyz"],
# ⁠ ["az","ba"],
# ⁠ ["acef"],
# ⁠ ["a","z"]
# ]
# 
# 
#

# @lc code=start
from itertools import groupby

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
        return [list(g) for _, g in groupby(sorted(strings, key=key), key)]
        
# @lc code=end

