#
# @lc app=leetcode id=1392 lang=python3
#
# [1392] Longest Happy Prefix
#
# https://leetcode.com/problems/longest-happy-prefix/description/
#
# algorithms
# Hard (40.91%)
# Likes:    272
# Dislikes: 16
# Total Accepted:    10.5K
# Total Submissions: 25.5K
# Testcase Example:  '"level"'
#
# A string is called a happy prefix if is a non-empty prefix which is also a
# suffix (excluding itself).
# 
# Given a string s. Return the longest happy prefix of s .
# 
# Return an empty string if no such prefix exists.
# 
# 
# Example 1:
# 
# 
# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"),
# and suffix ("l", "el", "vel", "evel"). The largest prefix which is also
# suffix is given by "l".
# 
# 
# Example 2:
# 
# 
# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can
# overlap in the original string.
# 
# 
# Example 3:
# 
# 
# Input: s = "leetcodeleet"
# Output: "leet"
# 
# 
# Example 4:
# 
# 
# Input: s = "a"
# Output: ""
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        res, l, r, MOD = 0, 0, 0, 10**9 + 7

        for i in range(len(s) - 1):
            l = (l * 128 + ord(s[i])) % MOD
            r = (r + pow(128, i, MOD) * ord(s[~i])) % MOD
            if l == r:
                res = i + 1
            
        return s[:res]
        
# @lc code=end

