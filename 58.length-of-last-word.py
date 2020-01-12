#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.29%)
# Likes:    456
# Dislikes: 1876
# Total Accepted:    304.1K
# Total Submissions: 941.1K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# 
# Input: "Hello World"
# Output: 5
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        slow = -1
        while slow >= -n and s[slow] == ' ':
            slow -= 1

        fast = slow

        while fast >= -n and s[fast] != ' ':
            fast -= 1

        return slow - fast
        
# @lc code=end

