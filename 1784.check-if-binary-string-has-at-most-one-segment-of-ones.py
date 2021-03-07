#
# @lc app=leetcode id=1784 lang=python3
#
# [1784] Check if Binary String Has at Most One Segment of Ones
#
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/
#
# algorithms
# Easy (41.98%)
# Likes:    23
# Dislikes: 61
# Total Accepted:    7.5K
# Total Submissions: 17.8K
# Testcase Example:  '"1001"'
#
# Given a binary string s ​​​​​without leading zeros, return true​​​ if s
# contains at most one contiguous segment of ones. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
# 
# 
# Example 2:
# 
# 
# Input: s = "110"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.
# 
# 
#

# @lc code=start
from itertools import groupby

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len([x for x in list(groupby(s)) if x[0] == '1']) == 1
        
# @lc code=end

