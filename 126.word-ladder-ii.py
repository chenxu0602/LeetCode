#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (18.47%)
# Likes:    1255
# Dislikes: 213
# Total Accepted:    141.1K
# Total Submissions: 735K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        # O(n^2 x k)
        wordList = set(wordList)
        res, layer = [], defaultdict(list)
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                else:
                    for i in range(len(word)):
                        for c in string.ascii_lowercase:
                            newWord = word[:i] + c + word[i+1:]
                            if newWord in wordList:
                                newlayer[newWord] += [j + [newWord] for j in layer[word]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res




        
# @lc code=end

