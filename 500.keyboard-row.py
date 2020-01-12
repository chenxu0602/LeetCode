#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (62.45%)
# Likes:    407
# Dislikes: 512
# Total Accepted:    91.5K
# Total Submissions: 146.5K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# 
# 
# 
# 
# Note:
# 
# 
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
# 
#
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        word_list = []
        top_row = set("qwertyuiop")
        mid_row = set("asdfghjkl")
        bot_row = set("zxcvbnm")

        for word in words:
            if set(word.lower()).issubset(top_row) or set(word.lower()).issubset(mid_row) or set(word.lower()).issubset(bot_row):
                word_list.append(word)
        return word_list
        

