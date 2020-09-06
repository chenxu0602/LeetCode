#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#
# https://leetcode.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (50.63%)
# Likes:    257
# Dislikes: 66
# Total Accepted:    14.1K
# Total Submissions: 27.8K
# Testcase Example:  '["time", "me", "bell"]'
#
# Given a list of words, we may encode it by writing a reference string S and a
# list of indexes A.
# 
# For example, if the list of words is ["time", "me", "bell"], we can write it
# as S = "time#bell#" and indexes = [0, 2, 5].
# 
# Then for each index, we will recover the word by reading from the reference
# string from that index until we reach a "#" character.
# 
# What is the length of the shortest reference string S possible that encodes
# the given words?
# 
# Example:
# 
# 
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 2000.
# 1 <= words[i].length <= 7.
# Each word has only lowercase letters.
# 
# 
#

# @lc code=start
from collections import defaultdict
import functools

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # Store Prefixes
        # Time  complexity: O(sum(w_i ^ 2)), where w_i is the length of words[i].
        # Space complexity: O(sum(w_i)), the space used in storing prefixes.
        # good = set(words)
        # for word in words:
        #     for i in range(1, len(word)):
        #         good.discard(word[i:])
        # return sum(len(word) + 1 for word in good)


        # Trie
        # Time  complexity: O(sum(w_i)), where w_i is the length of words[i].
        # Space complexity: O(sum(w_i)), the space used in storing prefixes.
        words = list(set(words))
        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        # the leaves of this trie (nodes with no children) represent words that have no suffix
        nodes = [functools.reduce(dict.__getitem__, word[::-1], trie) for word in words]
        
        # Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)
# @lc code=end

