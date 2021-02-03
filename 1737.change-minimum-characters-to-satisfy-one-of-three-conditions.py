#
# @lc app=leetcode id=1737 lang=python3
#
# [1737] Change Minimum Characters to Satisfy One of Three Conditions
#
# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/description/
#
# algorithms
# Medium (28.64%)
# Likes:    114
# Dislikes: 170
# Total Accepted:    4.9K
# Total Submissions: 17.1K
# Testcase Example:  '"aba"\n"caa"'
#
# You are given two strings a and b that consist of lowercase letters. In one
# operation, you can change any character in a or b to any lowercase letter.
# 
# Your goal is to satisfy one of the following three conditions:
# 
# 
# Every letter in a is strictly less than every letter in b in the
# alphabet.
# Every letter in b is strictly less than every letter in a in the
# alphabet.
# Both a and b consist of only one distinct letter.
# 
# 
# Return the minimum number of operations needed to achieve your goal.
# 
# 
# Example 1:
# 
# 
# Input: a = "aba", b = "caa"
# Output: 2
# Explanation: Consider the best way to make each condition true:
# 1) Change b to "ccc" in 2 operations, then every letter in a is less than
# every letter in b.
# 2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b
# is less than every letter in a.
# 3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of
# one distinct letter.
# The best way was done in 2 operations (either condition 1 or condition 3).
# 
# 
# Example 2:
# 
# 
# Input: a = "dabadd", b = "cda"
# Output: 3
# Explanation: The best way is to make condition 1 true by changing b to
# "eee".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= a.length, b.length <= 10^5
# a and b consist only of lowercase letters.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = map(len, (a, b))
        c1 = Counter(ord(c) - ord('a') for c in a)
        c2 = Counter(ord(c) - ord('a') for c in b)
        res = m + n - max((c1 + c2).values())

        for i in range(25):
            c1[i + 1] += c1[i]
            c2[i + 1] += c2[i]
            res = min(res, m - c1[i] + c2[i])
            res = min(res, n - c2[i] + c1[i])

        return res
        
# @lc code=end

