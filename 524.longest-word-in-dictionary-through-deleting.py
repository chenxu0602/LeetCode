#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (46.10%)
# Likes:    348
# Dislikes: 183
# Total Accepted:    46.3K
# Total Submissions: 100.2K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# Example 1:
# 
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# 
# 
# Note:
# 
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# 
# 
#
class Solution:
    def issubsequence(self, x, y):
        j = 0
        for i in range(len(y)):
            if x[j] == y[i]:
                j += 1
            if j == len(x):
                break
        return j == len(x)


    def findLongestWord(self, s: str, d: List[str]) -> str:
        # max_str = ""
        # for str in d:
        #     if self.issubsequence(str, s):
        #         if len(str) > len(max_str) or (len(str) == len(max_str) and str < max_str):
        #             max_str = str

        # return max_str

        for word in sorted(d, key=lambda w: (-len(w), w)):
            it = iter(s)
            if all(c in it for c in word): return word
        return ""

        

