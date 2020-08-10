#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (48.52%)
# Likes:    510
# Dislikes: 47
# Total Accepted:    80.2K
# Total Submissions: 165.1K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. You may
# assume that each word will contain only lower case letters. If no such two
# words exist, return 0.
# 
# Example 1:
# 
# 
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".
# 
# Example 2:
# 
# 
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4 
# Explanation: The two words can be "ab", "cd".
# 
# Example 3:
# 
# 
# Input: ["a","aa","aaa","aaaa"]
# Output: 0 
# Explanation: No such pair of words.
# 
# 
#

from functools import reduce 

from collections import defaultdict

class Solution:
    def maxProduct(self, words: List[str]) -> int:

        # Time  complexity: O(N^2 + L),  where NN is a number of words and LL is a total length of all words together. 
        # The precomputation takes O(L) time because we iterate over all characters in all words. 
        # Space complexity: O(N)
        # n = len(words)
        # masks = [0] * n
        # lens = [0] * n
        # bit_number = lambda ch: ord(ch) - ord('a')

        # for i in range(n):
        #     bitmask = 0
        #     for ch in words[i]:
        #         bitmask |= 1 << bit_number(ch)
        #     masks[i] = bitmask
        #     lens[i] = len(words[i])

        # max_val = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if masks[i] & masks[j] == 0:
        #             max_val = max(max_val, lens[i] * lens[j])

        # return max_val


        # hashmap = defaultdict(int)
        # bit_number = lambda ch: ord(ch) - ord('a')

        # for word in words:
        #     bitmask = 0
        #     for ch in word:
        #         bitmask |= 1 << bit_number(ch)
        #     hashmap[bitmask] = max(hashmap[bitmask], len(word))

        # max_prod = 0
        # for x in hashmap:
        #     for y in hashmap:
        #         if x & y == 0:
        #             max_prod = max(max_prod, hashmap[x] * hashmap[y])

        # return max_prod

        

        maskLen = {reduce(lambda x, y: x | y, [1 << (ord(c) - ord('a')) for c in word], 0) \
            : len(word) for word in sorted(words, key=lambda x: len(x))}.items()
        return max([x[1] * y[1] for i, x in enumerate(maskLen) for y in list(maskLen)[:i] if not (x[0] & y[0])] or [0])
        

