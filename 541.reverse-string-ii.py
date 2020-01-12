#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (45.78%)
# Likes:    261
# Dislikes: 794
# Total Accepted:    63.1K
# Total Submissions: 137.9K
# Testcase Example:  '"abcdefg"\n2'
#
# 
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string. If there are
# less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k
# characters and left the other as original.
# 
# 
# Example:
# 
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# 
# 
# 
# Restrictions: 
# 
# ⁠The string consists of lower English letters only.
# ⁠Length of the given string and k will in the range [1, 10000]
# 
#
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
        """

        if not s: return s
        i, j = 0, k - 1
        chars = [c for c in s]
        while i < len(s):
            x, y = i, min(j, len(s)-1)
            while x < y:
                chars[x], chars[y] = chars[y], chars[x]
                x, y = x + 1, y - 1
            i, j = i + 2*k, j + 2*k 
        return "".join(chars)

