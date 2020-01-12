#
# @lc app=leetcode id=1055 lang=python3
#
# [1055] Shortest Way to Form String
#
# https://leetcode.com/problems/shortest-way-to-form-string/description/
#
# algorithms
# Medium (58.93%)
# Likes:    126
# Dislikes: 7
# Total Accepted:    8.1K
# Total Submissions: 13.9K
# Testcase Example:  '"abc"\n"abcbc"'
#
# From any string, we can form a subsequence of that string by deleting some
# number of characters (possibly no deletions).
# 
# Given two strings source and target, return the minimum number of
# subsequences of source such that their concatenation equals target. If the
# task is impossible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are
# subsequences of source "abc".
# 
# 
# Example 2:
# 
# 
# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of
# source string due to the character "d" in target string.
# 
# 
# Example 3:
# 
# 
# Input: source = "xyz", target = "xzyxz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" +
# "xz".
# 
# 
# Constraints:
# 
# 
# Both the source and target strings consist of only lowercase English letters
# from "a"-"z".
# The lengths of source and target string are between 1 and 1000.
# 
#
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i, minimum = 0, 1

        for c in target:
            i = source.find(c, i)
            if i == -1:
                i = source.find(c)
                minimum += 1
                if i == -1:
                    return i

            i += 1

        return minimum



