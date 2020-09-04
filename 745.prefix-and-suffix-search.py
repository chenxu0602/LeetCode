#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#
# https://leetcode.com/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (32.98%)
# Likes:    269
# Dislikes: 181
# Total Accepted:    16.2K
# Total Submissions: 49.2K
# Testcase Example:  '["WordFilter","f"]\n[[["apple"]],["a","e"]]'
#
# Given many words, words[i] has weight i.
# 
# Design a class WordFilter that supports one function, WordFilter.f(String
# prefix, String suffix). It will return the word with given prefix and suffix
# with maximum weight. If no word exists, return -1.
# 
# Examples:
# 
# 
# Input:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1
# 
# 
# 
# 
# Note:
# 
# 
# words has length in range [1, 15000].
# For each test case, up to words.length queries WordFilter.f may be made.
# words[i] has length in range [1, 10].
# prefix, suffix have lengths in range [0, 10].
# words[i] and prefix, suffix queries consist of lowercase letters only.
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict

Trie = lambda: defaultdict(Trie)
WEIGHT = False

class WordFilter:

    def __init__(self, words: List[str]):
        # Time  complexity: O(NK^2 + Q) where N is the number of words, K is the maximum length of a word,
        # Q is the number of queries.
        # Spase complexity: O(NK^2)
        # self.pre_suf_map = {}
        # for word in range(len(words)):
        #     length = len(words[word])
        #     for i in range(length + 1):
        #         for j in reversed(range(length + 1)):
        #             if i > 10 or (length - j) > 10:
        #                 continue
        #             comb = words[word][:i] + '.' + words[word][j:]
        #             self.pre_suf_map[comb] = word
        

        # Trie of Suffix Wrapped Words
        # Time  complexity: O(NK^2 + QK) where N is the number of words, K is the maximum length of a word,
        # Q is the number of queries.
        # Spase complexity: O(NK^2)
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix: str, suffix: str) -> int:
        # pre_suf = prefix + '.' + suffix
        # if pre_suf in self.pre_suf_map:
        #     return self.pre_suf_map[pre_suf]
        # return -1
        

        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end

