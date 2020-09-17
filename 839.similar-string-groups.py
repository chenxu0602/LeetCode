#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#
# https://leetcode.com/problems/similar-string-groups/description/
#
# algorithms
# Hard (35.33%)
# Likes:    185
# Dislikes: 63
# Total Accepted:    10.7K
# Total Submissions: 30.2K
# Testcase Example:  '["tars","rats","arts","star"]'
#
# Two strings X and Y are similar if we can swap two letters (in different
# positions) of X, so that it equals Y.
# 
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
# and "rats" and "arts" are similar, but "star" is not similar to "tars",
# "rats", or "arts".
# 
# Together, these form two connected groups by similarity: {"tars", "rats",
# "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group
# even though they are not similar.  Formally, each group is such that a word
# is in the group if and only if it is similar to at least one other word in
# the group.
# 
# We are given a list A of strings.  Every string in A is an anagram of every
# other string in A.  How many groups are there?
# 
# Example 1:
# 
# 
# Input: ["tars","rats","arts","star"]
# Output: 2
# 
# Note:
# 
# 
# A.length <= 2000
# A[i].length <= 1000
# A.length * A[i].length <= 20000
# All words in A consist of lowercase letters only.
# All words in A have the same length and are anagrams of each other.
# The judging time limit has been increased for this question.
# 
# 
#

import itertools
from collections import defaultdict

class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: return False
        if self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution:

    def numSimilarGroups(self, A: List[str]) -> int:
        A = list(set(A))
        N, W = len(A), len(A[0])

        def similar(word1, word2):
            diff = 0
            for x, y in zip(word1, word2):
                if x != y:
                    diff += 1
            return diff <= 2

        dsu = DSU(N)

        if N < W * W:
            for (i1, word1), (i2, word2) in itertools.combinations(enumerate(A), 2):
                if similar(word1, word2):
                    dsu.union(i1, i2)
        else:
            buckets = defaultdict(set)
            for i, word in enumerate(A):
                L = list(word)
                for j0, j1 in itertools.combinations(range(W), 2):
                    L[j0], L[j1] = L[j1], L[j0]
                    buckets["".join(L)].add(i)
                    L[j0], L[j1] = L[j1], L[j0]

            for i1, word in enumerate(A):
                for i2 in buckets[word]:
                    dsu.union(i1, i2)

        return sum(dsu.par[x] == x for x in range(N))



        

