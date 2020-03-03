#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (33.79%)
# Likes:    1270
# Dislikes: 70
# Total Accepted:    150K
# Total Submissions: 443.6K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' + '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#

# @lc code=start
from collections import defaultdict
from functools import reduce

Trie = lambda: defaultdict(Trie)
END = '#'

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        reduce(dict.__getitem__, word, self.root)[END] = ""
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node: Trie, word: str) -> None:
        if not word:
            if END in node:
                self.res = True
            return

        if word[0] == '.':
            for c in node:
                self.dfs(node[c], word[1:])
        else:
            if node:
                node = node[word[0]]
                if not node:
                    return
                self.dfs(node, word[1:])
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

