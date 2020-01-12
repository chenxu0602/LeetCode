#
# @lc app=leetcode id=616 lang=python3
#
# [616] Add Bold Tag in String
#
# https://leetcode.com/problems/add-bold-tag-in-string/description/
#
# algorithms
# Medium (39.51%)
# Likes:    338
# Dislikes: 37
# Total Accepted:    25.2K
# Total Submissions: 63.5K
# Testcase Example:  '"abcxyz123"\n["abc","123"]'
#
# Given a string s and a list of strings dict, you need to add a closed pair of
# bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two
# such substrings overlap, you need to wrap them together by only one pair of
# closed bold tag. Also, if two substrings wrapped by bold tags are
# consecutive, you need to combine them. 
# 
# Example 1:
# 
# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# 
# 
# 
# Example 2:
# 
# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# 
# 
# 
# Note:
# 
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000]. 
# 
# 
#
import itertools

class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        n = len(s)
        mask = [False] * n
        for i in range(n):
            prefix = s[i:]
            for word in dict:
                if prefix.startswith(word):
                    for j in range(i, min(i+len(word), n)):
                        mask[j] = True

        ans = []
        for incl, grp in itertools.groupby(zip(s, mask), lambda z: z[1]):
            if incl:
                ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl:
                ans.append("</b>")

        return "".join(ans)

        

