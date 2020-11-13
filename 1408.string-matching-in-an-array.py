#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#
# https://leetcode.com/problems/string-matching-in-an-array/description/
#
# algorithms
# Easy (62.59%)
# Likes:    224
# Dislikes: 51
# Total Accepted:    29.2K
# Total Submissions: 46.7K
# Testcase Example:  '["mass","as","hero","superhero"]'
#
# Given an array of string words. Return all strings in words which is
# substring of another word in any order. 
# 
# String words[i] is substring of words[j], if can be obtained removing some
# characters to left and/or right side of words[j].
# 
# 
# Example 1:
# 
# 
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of
# "superhero".
# ["hero","as"] is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# 
# 
# Example 3:
# 
# 
# Input: words = ["blue","green","bu"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# It's guaranteed that words[i] will be unique.
# 
#

# @lc code=start
from collections import defaultdict
from functools import reduce

class Trie(defaultdict):
    def __init__(self):
        self.cnt = 0
        super().__init__(Trie)

    def add(cur, x):
        for c in x:
            cur = cur[c]
            cur.cnt += 1

    def get(cur, x):
        return reduce(getitem, x, cur).cnt > 1

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # arr = ' '.join(words)
        # subStr = [i for i in words if arr.count(i) >= 2]
        # return subStr


        # words = sorted(words, key=len)
        # res = []
        # for i in range(len(words)):
        #     for j in range(i + 1, len(words)):
        #         if words[i] in words[j]:
        #             res.append(words[i])
        #             break
        # return res
        

        # Suffix trie 
        # O(NlogN + N x S ^ 2)
        # def add(word: str):
        #     node = trie
        #     for c in word:
        #         node = node.setdefault(c, {})

        # def get(word: str) -> bool:
        #     node = trie
        #     for c in word:
        #         if (node := node.get(c)) is None:
        #             return False
        #     return True


        # words.sort(key=len, reverse=True)
        # trie, result = {}, []
        # for word in words:
        #     if get(word):
        #         result.append(word)
        #     for i in range(len(word)):
        #         add(word[i:])
        # return result


        # It utilizes counting on trie nodes in suffix trie and can prevent to perform sorting at first.
        # O(N x S ^ 2)
        # def add(word: str):
        #     node = trie 
        #     for c in word:
        #         node = node.setdefault(c, {})
        #         node['#'] = node.get('#', 0) + 1

        # def get(word: str) -> bool:
        #     node = trie
        #     for c in word:
        #         if (node := node.get(c)) is None:
        #             return False
        #     return node['#'] > 1

        # trie = {}
        # for word in words:
        #     for i in range(len(word)):
        #         add(word[i:])
        # return [word for word in words if get(word)]


        root = Trie()
        for word in words:
            for i in range(len(word)):
                root.add(word[i:])
        return list(filter(root.get, words))

        
# @lc code=end

