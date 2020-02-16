#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
#
# algorithms
# Medium (71.62%)
# Likes:    478
# Dislikes: 36
# Total Accepted:    47.1K
# Total Submissions: 65.8K
# Testcase Example:  '"())"'
#
# Given a string S of '(' and ')' parentheses, we add the minimum number of
# parentheses ( '(' or ')', and in any positions ) so that the resulting
# parentheses string is valid.
# 
# Formally, a parentheses string is valid if and only if:
# 
# 
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# Given a parentheses string, return the minimum number of parentheses we must
# add to make the resulting string valid.
# 
# 
# 
# Example 1:
# 
# 
# Input: "())"
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: "((("
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: "()"
# Output: 0
# 
# 
# 
# Example 4:
# 
# 
# Input: "()))(("
# Output: 4
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 1000
# S only consists of '(' and ')' characters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, S: str) -> int:

        # l = list(S)
        # if len(l) == 0: return 0
        # temp = [l[0]]
        # for i in range(1, len(l)):
        #     if l[i] == '(':
        #         temp.append(l[i])
        #     elif l[i] == ')' and len(temp) > 0 and temp[-1] == '(':
        #         temp.pop()
        #     else:
        #         temp.append(l[i])
        # return len(temp)

        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
        
# @lc code=end

