#
# @lc app=leetcode id=854 lang=python3
#
# [854] K-Similar Strings
#
# https://leetcode.com/problems/k-similar-strings/description/
#
# algorithms
# Hard (34.67%)
# Likes:    215
# Dislikes: 24
# Total Accepted:    9.8K
# Total Submissions: 27.9K
# Testcase Example:  '"ab"\n"ba"'
#
# Strings A and B are K-similar (for some non-negative integer K) if we can
# swap the positions of two letters in A exactly K times so that the resulting
# string equals B.
# 
# Given two anagrams A and B, return the smallest K for which A and B are
# K-similar.
# 
# Example 1:
# 
# 
# Input: A = "ab", B = "ba"
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: A = "abc", B = "bca"
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: A = "abac", B = "baca"
# Output: 2
# 
# 
# 
# Example 4:
# 
# 
# Input: A = "aabc", B = "abca"
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length == B.length <= 20
# A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e',
# 'f'}
# 
# 
#
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def neighbors(x):
            i = 0
            while x[i] == B[i]:
                i += 1
            for j in range(i+1, len(x)):
                if x[j] == B[i]:
                    yield x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]

        q, seen = [(A, 0)], {A}

        for x, d in q:
            if x == B: 
                return d
            for y in neighbors(x):
                if y not in seen:
                    seen.add(y)
                    q.append((y, d+1))
        

