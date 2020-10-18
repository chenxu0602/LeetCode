#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (59.32%)
# Likes:    211
# Dislikes: 10
# Total Accepted:    11.4K
# Total Submissions: 19.1K
# Testcase Example:  '"(abcd)"'
#
# You are given a string s that consists of lower case English letters and
# brackets. 
# 
# Reverse the strings in each pair of matching parentheses, starting from the
# innermost one.
# 
# Your result should not contain any brackets.
# 
# 
# Example 1:
# 
# 
# Input: s = "(abcd)"
# Output: "dcba"
# 
# 
# Example 2:
# 
# 
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is
# reversed.
# 
# 
# Example 3:
# 
# 
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally,
# the whole string.
# 
# 
# Example 4:
# 
# 
# Input: s = "a(bcdefghijkl(mno)p)q"
# Output: "apmnolkjihgfedcbq"
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It's guaranteed that all parentheses are balanced.
# 
# 
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # stack = [""]
        # for c in s:
        #     if c == '(':
        #         stack.append("")
        #     elif c == ')':
        #         add = stack.pop()[::-1]
        #         stack[-1] += add
        #     else:
        #         stack[-1] += c
        # return stack.pop()


        opened, pair = [], {}
        for i, c in enumerate(s):
            if c == '(':
                opened.append(i)
            elif c == ')':
                j = opened.pop()
                pair[i], pair[j] = j, i

        res = []
        i, d = 0, 1
        while i < len(s):
            if s[i] in "()":
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return "".join(res)
        
# @lc code=end

