#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#
# https://leetcode.com/problems/scramble-string/description/
#
# algorithms
# Hard (32.81%)
# Likes:    415
# Dislikes: 635
# Total Accepted:    103.5K
# Total Submissions: 313.9K
# Testcase Example:  '"great"\n"rgeat"'
#
# Given a string s1, we may represent it as a binary tree by partitioning it to
# two non-empty substrings recursively.
# 
# Below is one possible representation of s1 = "great":
# 
# 
# ⁠   great
# ⁠  /    \
# ⁠ gr    eat
# ⁠/ \    /  \
# g   r  e   at
# ⁠          / \
# ⁠         a   t
# 
# 
# To scramble the string, we may choose any non-leaf node and swap its two
# children.
# 
# For example, if we choose the node "gr" and swap its two children, it
# produces a scrambled string "rgeat".
# 
# 
# ⁠   rgeat
# ⁠  /    \
# ⁠ rg    eat
# ⁠/ \    /  \
# r   g  e   at
# ⁠          / \
# ⁠         a   t
# 
# 
# We say that "rgeat" is a scrambled string of "great".
# 
# Similarly, if we continue to swap the children of nodes "eat" and "at", it
# produces a scrambled string "rgtae".
# 
# 
# ⁠   rgtae
# ⁠  /    \
# ⁠ rg    tae
# ⁠/ \    /  \
# r   g  ta  e
# ⁠      / \
# ⁠     t   a
# 
# 
# We say that "rgtae" is a scrambled string of "great".
# 
# Given two strings s1 and s2 of the same length, determine if s2 is a
# scrambled string of s1.
# 
# Example 1:
# 
# 
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if not len(s1) == len(s2): return False

        if s1 == s2: return True

        l1, l2 = map(sorted, (s1, s2))

        if not l1 == l2: return False

        n = len(s1)

        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True

        return False


        
# @lc code=end

