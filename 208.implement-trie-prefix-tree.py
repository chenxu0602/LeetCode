#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (43.48%)
# Likes:    2332
# Dislikes: 41
# Total Accepted:    238.7K
# Total Submissions: 547.5K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' + '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#

# @lc code=start
from collections import defaultdict
from functools import reduce

T = lambda: defaultdict(T)
END = '#'

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = T()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        reduce(dict.__getitem__, word, self.trie)[END] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.trie
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return curr[END]
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.trie
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

