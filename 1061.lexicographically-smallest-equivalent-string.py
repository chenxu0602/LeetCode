#
# @lc app=leetcode id=1061 lang=python3
#
# [1061] Lexicographically Smallest Equivalent String
#
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/
#
# algorithms
# Medium (62.99%)
# Likes:    29
# Dislikes: 1
# Total Accepted:    1.4K
# Total Submissions: 2.3K
# Testcase Example:  '"parker"\n"morris"\n"parser"'
#
# Given strings A and B of the same length, we say A[i] and B[i] are equivalent
# characters. For example, if A = "abc" and B = "cde", then we have 'a' == 'c',
# 'b' == 'd', 'c' == 'e'.
# 
# Equivalent characters follow the usual rules of any equivalence
# relation:
# 
# 
# Reflexivity: 'a' == 'a'
# Symmetry: 'a' == 'b' implies 'b' == 'a'
# Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'
# 
# 
# For example, given the equivalency information from A and B above, S = "eed",
# "acd", and "aab" are equivalent strings, and "aab" is the lexicographically
# smallest equivalent string of S.
# 
# Return the lexicographically smallest equivalent string of S by using the
# equivalency information from A and B.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = "parker", B = "morris", S = "parser"
# Output: "makkek"
# Explanation: Based on the equivalency information in A and B, we can group
# their characters as [m,p], [a,o], [k,r,s], [e,i]. The characters in each
# group are equivalent and sorted in lexicographical order. So the answer is
# "makkek".
# 
# 
# Example 2:
# 
# 
# Input: A = "hello", B = "world", S = "hold"
# Output: "hdld"
# Explanation:  Based on the equivalency information in A and B, we can group
# their characters as [h,w], [d,e,o], [l,r]. So only the second letter 'o' in S
# is changed to 'd', the answer is "hdld".
# 
# 
# Example 3:
# 
# 
# Input: A = "leetcode", B = "programs", S = "sourcecode"
# Output: "aauaaaaada"
# Explanation:  We group the equivalent characters in A and B as [a,o,e,r,s,c],
# [l,p], [g,t] and [d,m], thus all letters in S except 'u' and 'd' are
# transformed to 'a', the answer is "aauaaaaada".
# 
# 
# 
# 
# Note:
# 
# 
# String A, B and S consist of only lowercase English letters from 'a' -
# 'z'.
# The lengths of string A, B and S are between 1 and 1000.
# String A and B are of the same length.
# 
#
import string 

class UF:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if xr < yr:
            self.p[yr] = xr
        else:
            self.p[xr] = yr

class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:

        """
        def root(c):
            return c if parent[c] == c else root(parent[c])

        parent = {s: s for s in string.ascii_lowercase}

        for a, b in zip(A, B):
            p1, p2 = root(a), root(b)
            if p1 <= p2:
                parent[p2] = p1
            else:
                parent[p1] = p2

        return "".join(root(s) for s in S)
        """

        uf = UF(26)
        for a, b in zip(A, B):
            if not a == b:
                uf.union(ord(a) - ord('a'), ord(b) - ord('a'))

        return "".join([chr(uf.find(ord(c) - ord('a')) + ord('a')) for c in S])
        

