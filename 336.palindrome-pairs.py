#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (31.02%)
# Likes:    789
# Dislikes: 105
# Total Accepted:    70.9K
# Total Submissions: 228.2K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# Given a list of unique words, find all pairs of distinct indices (i, j) in
# the given list, so that the concatenation of the two words, i.e. words[i] +
# words[j] is a palindrome.
# 
# Example 1:
# 
# 
# 
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]] 
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]] 
# Explanation: The palindromes are ["battab","tabbat"]
# 
# 
# 
# 
#
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                prefix = word[:j]
                suffix = word[j:]
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back], k])
                
                if j != n and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])

        return valid_pals
        

