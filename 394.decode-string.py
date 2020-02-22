#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (47.89%)
# Likes:    2407
# Dislikes: 124
# Total Accepted:    164.5K
# Total Submissions: 343.4K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# Examples:
# 
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack, curNum, curString = [], 0, ""

        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString, curNum = "", 0
            elif c == ']':
                num, prevString = stack.pop(), stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c

        return curString
        
# @lc code=end

