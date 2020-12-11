#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#
# https://leetcode.com/problems/goal-parser-interpretation/description/
#
# algorithms
# Easy (88.32%)
# Likes:    57
# Dislikes: 9
# Total Accepted:    11.3K
# Total Submissions: 12.9K
# Testcase Example:  '"G()(al)"'
#
# You own a Goal Parser that can interpret a string command. The command
# consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal
# Parser will interpret "G" as the string "G", "()" as the string "o", and
# "(al)" as the string "al". The interpreted strings are then concatenated in
# the original order.
# 
# Given the string command, return the Goal Parser's interpretation of
# command.
# 
# 
# Example 1:
# 
# 
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# 
# 
# Example 2:
# 
# 
# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# 
# 
# Example 3:
# 
# 
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= command.length <= 100
# command consists of "G", "()", and/or "(al)" in some order.
# 
# 
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')
        
# @lc code=end

