#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (27.24%)
# Likes:    2735
# Dislikes: 119
# Total Accepted:    247K
# Total Submissions: 906.5K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        """
        ans, stack = 0, [-1]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans
        """

        left = right = maxlength = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif left <= right:
                left = right = 0

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif left >= right:
                left = right = 0

        return maxlength


        
# @lc code=end

