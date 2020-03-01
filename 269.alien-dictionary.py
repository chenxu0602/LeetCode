#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (33.86%)
# Likes:    1336
# Dislikes: 258
# Total Accepted:    114.5K
# Total Submissions: 337.9K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language which uses the latin alphabet. However, the
# order among letters are unknown to you. You receive a list of non-empty words
# from the dictionary, where words are sorted lexicographically by the rules of
# this new language. Derive the order of letters in this language.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ "wrt",
# ⁠ "wrf",
# ⁠ "er",
# ⁠ "ett",
# ⁠ "rftt"
# ]
# 
# Output: "wertf"
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ⁠ "z",
# ⁠ "x"
# ]
# 
# Output: "zx"
# 
# 
# Example 3:
# 
# 
# Input:
# [
# ⁠ "z",
# ⁠ "x",
# ⁠ "z"
# ] 
# 
# Output: "" 
# 
# Explanation: The order is invalid, so return "".
# 
# 
# Note:
# 
# 
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the
# given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is
# fine.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        pre, suc = defaultdict(set), defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break

        chars = set("".join(words))
        free = chars - set(pre)
        order = ""

        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)

        return order * (set(order) == chars)
        
# @lc code=end

