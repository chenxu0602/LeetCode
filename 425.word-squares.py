#
# @lc app=leetcode id=425 lang=python3
#
# [425] Word Squares
#
# https://leetcode.com/problems/word-squares/description/
#
# algorithms
# Hard (44.50%)
# Likes:    356
# Dislikes: 31
# Total Accepted:    24.8K
# Total Submissions: 55.8K
# Testcase Example:  '["area","lead","wall","lady","ball"]'
#
# Given a set of words (without duplicates), find all word squares you can
# build from them.
# 
# A sequence of words forms a valid word square if the k^th row and column read
# the exact same string, where 0 ≤ k < max(numRows, numColumns).
# 
# For example, the word sequence ["ball","area","lead","lady"] forms a word
# square because each word reads the same both horizontally and vertically.
# 
# 
# b a l l
# a r e a
# l e a d
# l a d y
# 
# 
# Note:
# 
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# 
# 
# 
# Example 1:
# 
# Input:
# ["area","lead","wall","lady","ball"]
# 
# Output:
# [
# ⁠ [ "wall",
# ⁠   "area",
# ⁠   "lead",
# ⁠   "lady"
# ⁠ ],
# ⁠ [ "ball",
# ⁠   "area",
# ⁠   "lead",
# ⁠   "lady"
# ⁠ ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).
# 
# 
# 
# Example 2:
# 
# Input:
# ["abat","baba","atan","atal"]
# 
# Output:
# [
# ⁠ [ "baba",
# ⁠   "abat",
# ⁠   "baba",
# ⁠   "atan"
# ⁠ ],
# ⁠ [ "baba",
# ⁠   "abat",
# ⁠   "baba",
# ⁠   "atal"
# ⁠ ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).
# 
# 
#
from collections import defaultdict

class Solution:

    def build(self, square, n):
        if len(square) == n:
            self.squares.append(square)
            return

        for word in self.fulls["".join(list(zip(*square))[len(square)])]:
            self.build(square + [word], n)

    def wordSquares(self, words: List[str]) -> List[List[str]]:

        n = len(words[0])
        self.fulls = defaultdict(list)
        for word in words:
            for i in range(n):
                self.fulls[word[:i]].append(word)

        self.squares = []
        for word in words:
            self.build([word], n)

        return self.squares
        
        

