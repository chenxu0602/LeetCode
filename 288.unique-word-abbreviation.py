#
# @lc app=leetcode id=288 lang=python3
#
# [288] Unique Word Abbreviation
#
# https://leetcode.com/problems/unique-word-abbreviation/description/
#
# algorithms
# Medium (20.04%)
# Likes:    66
# Dislikes: 885
# Total Accepted:    41.9K
# Total Submissions: 209.2K
# Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]\n' +
#
# An abbreviation of a word follows the form <first letter><number><last
# letter>. Below are some examples of word abbreviations:
# 
# 
# a) it                      --> it    (no abbreviation)
# 
# ⁠    1
# ⁠    ↓
# b) d|o|g                   --> d1g
# 
# ⁠             1    1  1
# ⁠    1---5----0----5--8
# ⁠    ↓   ↓    ↓    ↓  ↓    
# c) i|nternationalizatio|n  --> i18n
# 
# ⁠             1
# ⁠    1---5----0
# ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# 
# 
# Assume you have a dictionary and given a word, find whether its abbreviation
# is unique in the dictionary. A word's abbreviation is unique if no other word
# from the dictionary has the same abbreviation.
# 
# Example:
# 
# 
# Given dictionary = [ "deer", "door", "cake", "card" ]
# 
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
# 
# 
#

from collections import defaultdict

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = defaultdict(set)
        for s in dictionary:
            val = s
            if len(s) > 2:
                s = s[0] + str(len(s)-2) + s[-1]
            self.dic[s].add(val)
        

    def isUnique(self, word: str) -> bool:
        val = word
        if len(word) > 2:
            word = word[0] + str(len(word)-2) + word[-1] 

        return len(self.dic[word]) == 0 or (len(self.dic[word]) == 1 and val == list(self.dic[word])[0])


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

