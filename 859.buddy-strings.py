#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/description/
#
# algorithms
# Easy (27.77%)
# Likes:    359
# Dislikes: 216
# Total Accepted:    30.3K
# Total Submissions: 108.7K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings A and B of lowercase letters, return true if and only if we
# can swap two letters in A so that the result equals B.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: A = "ab", B = "ba"
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: A = "ab", B = "ab"
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: A = "aa", B = "aa"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: A = "", B = "aa"
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        C, A, B = [i for i in range(len(A)) if A[i] != B[i]], list(A), list(B)
        if not C and len(A) == len(B):
            for i in A:
                if A.count(i) > 1:
                    return True
        elif len(C) == 2 and A[C[0]] == B[C[1]] and A[C[1]] == B[C[0]]: 
            return True
        return False

        
        

