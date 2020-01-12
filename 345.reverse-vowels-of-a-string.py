#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (41.53%)
# Likes:    389
# Dislikes: 722
# Total Accepted:    158.6K
# Total Submissions: 381.2K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#
import re 

class Solution:
    def reverseVowels(self, s: str) -> str:

#        vowels = (c for c in reversed(s) if c in "aeiouAEIOU")
#        return re.sub("(?i)[aeiou]", lambda m: next(vowels), s)

        s, n, vowels = list(s), len(s), {'a', 'e', 'i', 'o', 'u'}
        low, high = 0, n - 1

        while low < high:
            while low < n and s[low].lower() not in vowels:
                low += 1
            while high >= 0 and s[high].lower() not in vowels:
                high -= 1

            if low >= high:
               break 

            s[low], s[high] = s[high], s[low]

            low += 1
            high -= 1

        return ''.join(s)
        

