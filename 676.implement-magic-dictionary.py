#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#
# https://leetcode.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (51.80%)
# Likes:    391
# Dislikes: 101
# Total Accepted:    27.5K
# Total Submissions: 52.9K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n' +
#
# 
# Implement a magic directory with buildDict, and search methods.
# 
# 
# 
# For the method buildDict, you'll be given a list of non-repetitive words to
# build a dictionary.
# 
# 
# 
# For the method search, you'll be given a word, and judge whether if you
# modify exactly one character into another character in this word, the
# modified word is in the dictionary you just built.
# 
# 
# Example 1:
# 
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# 
# 
# 
# Note:
# 
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think
# about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class
# MagicDictionary, as static/class variables are persisted across multiple test
# cases. Please see here for more details.
# 
# 
#

from collections import defaultdict

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = defaultdict(list)        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.buckets[len(word)].append(word)
        
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return any(sum(a!=b for a, b in zip(word, candidate)) == 1 for candidate in self.buckets[len(word)])
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

