#
# @lc app=leetcode id=1234 lang=python3
#
# [1234] Replace the Substring for Balanced String
#
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/description/
#
# algorithms
# Medium (31.14%)
# Likes:    154
# Dislikes: 32
# Total Accepted:    6.6K
# Total Submissions: 21.1K
# Testcase Example:  '"QWER"'
#
# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E'
# and 'R'.
# 
# A string is said to be balanced if each of its characters appears n/4 times
# where n is the length of the string.
# 
# Return the minimum length of the substring that can be replaced with any
# other string of the same length to make the original string s balanced.
# 
# Return 0 if the string is already balanced.
# 
# 
# Example 1:
# 
# 
# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced.
# 
# Example 2:
# 
# 
# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is
# balanced.
# 
# 
# Example 3:
# 
# 
# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER". 
# 
# 
# Example 4:
# 
# 
# Input: s = "QQQQ"
# Output: 3
# Explanation: We can replace the last 3 'Q' to make s = "QWER".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s.length is a multiple of 4
# s contains only 'Q', 'W', 'E' and 'R'.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n // 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res

        
# @lc code=end

