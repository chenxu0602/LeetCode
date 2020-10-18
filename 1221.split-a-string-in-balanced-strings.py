#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#
# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
#
# algorithms
# Easy (83.08%)
# Likes:    727
# Dislikes: 476
# Total Accepted:    106.7K
# Total Submissions: 127.3K
# Testcase Example:  '"RLRRLLRLRL"'
#
# Balanced strings are those who have equal quantity of 'L' and 'R'
# characters.
# 
# Given a balanced string s split it in the maximum amount of balanced
# strings.
# 
# Return the maximum amount of splitted balanced strings.
# 
# 
# Example 1:
# 
# 
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring
# contains same number of 'L' and 'R'.
# 
# 
# Example 2:
# 
# 
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring
# contains same number of 'L' and 'R'.
# 
# 
# Example 3:
# 
# 
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
# 
# 
# Example 4:
# 
# 
# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", since each substring
# contains an equal number of 'L' and 'R'
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s[i] = 'L' or 'R'
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return list(itertools.accumulate(1 if c == 'L' else -1 for c in s)).count(0)
        
# @lc code=end

