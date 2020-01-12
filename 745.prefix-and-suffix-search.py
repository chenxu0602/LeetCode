#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#
# https://leetcode.com/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (31.40%)
# Likes:    220
# Dislikes: 161
# Total Accepted:    13.4K
# Total Submissions: 42.8K
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
class WordFilter:

    def __init__(self, words: List[str]):
        self.pre_suf_map = {}
        for word in range(len(words)):
            length = len(words[word])
            for i in range(length+1):
                for j in reversed(range(length+1)):
                    if (i > 10 or (length - j) > 10) > length:
                        continue
                    comb = words[word][:i] + "." + words[word][j:]
                    self.pre_suf_map[comb] = word
        

    def f(self, prefix: str, suffix: str) -> int:
        pref_suf = prefix + "." + suffix
        if pref_suf in self.pre_suf_map:
            return self.pre_suf_map[pref_suf]

        return -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

