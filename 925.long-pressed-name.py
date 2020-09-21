#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (40.92%)
# Likes:    726
# Dislikes: 125
# Total Accepted:    49.8K
# Total Submissions: 125K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard.  Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
# 
# You examine the typed characters of the keyboard.  Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
# 
# 
# Example 1:
# 
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# 
# Example 2:
# 
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed
# output.
# 
# 
# Example 3:
# 
# 
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# 
# 
# Example 4:
# 
# 
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= name.length <= 1000
# 1 <= typed.length <= 1000
# The characters of name and typed are lowercase letters.
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Group into Blocks
        # Time  complexity: O(N + T), where N and T are the lengths of name and typed.
        # Space complexity: O(N + T)
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))




        
# @lc code=end

