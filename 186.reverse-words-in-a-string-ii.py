#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#
# https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
#
# algorithms
# Medium (38.72%)
# Likes:    328
# Dislikes: 87
# Total Accepted:    73.4K
# Total Submissions: 184.5K
# Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
#
# Given an input string , reverse the string word by word. 
# 
# Example:
# 
# 
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# 
# Note: 
# 
# 
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# 
# 
# Follow up: Could you do it in-place without allocating extra space?
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        """
        s[:] = list(" ".join("".join(s).split()[::-1]))
        """

        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        reverse(s, 0, len(s)-1)
        beg = 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverse(s, beg, i-1)
                beg = i + 1
            elif i == len(s)-1:
                reverse(s, beg, i)
        
# @lc code=end

