#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
#
# algorithms
# Easy (55.96%)
# Likes:    294
# Dislikes: 102
# Total Accepted:    36.7K
# Total Submissions: 65.7K
# Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
#
# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.
# 
# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted
# lexicographicaly in this alien language.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is
# sorted.
# 
# 
# 
# Example 2:
# 
# 
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] >
# words[1], hence the sequence is unsorted.
# 
# 
# 
# Example 3:
# 
# 
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is
# shorter (in size.) According to lexicographical rules "apple" > "app",
# because 'l' > '∅', where '∅' is defined as the blank character which is less
# than any other character (More info).
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are english lowercase letters.
# 
# 
# 
# 
# 
#
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # m = {c: i for i, c in enumerate(order)}
        # words = [[m[c] for c in w] for w in words]
        # return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

        order_index = {c: i for i, c in enumerate(order)}

        for w1, w2 in zip(words, words[1:]):
            for k in range(min(len(w1), len(w2))):
                if w1[k] != w2[k]:
                    if order_index[w1[k]] > order_index[w2[k]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False

        return True
        

