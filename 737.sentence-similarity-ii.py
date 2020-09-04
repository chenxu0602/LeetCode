#
# @lc app=leetcode id=737 lang=python3
#
# [737] Sentence Similarity II
#
# https://leetcode.com/problems/sentence-similarity-ii/description/
#
# algorithms
# Medium (43.87%)
# Likes:    321
# Dislikes: 18
# Total Accepted:    25.1K
# Total Submissions: 57.3K
# Testcase Example:  '["great","acting","skills"]\n["fine","drama","talent"]\n' +
#
# Given two sentences words1, words2 (each represented as an array of strings),
# and a list of similar word pairs pairs, determine if two sentences are
# similar.
# 
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine",
# "drama", "talent"] are similar, if the similar word pairs are pairs =
# [["great", "good"], ["fine", "good"], ["acting","drama"],
# ["skills","talent"]].
# 
# Note that the similarity relation is transitive. For example, if "great" and
# "good" are similar, and "fine" and "good" are similar, then "great" and
# "fine" are similar.
# 
# Similarity is also symmetric. For example, "great" and "fine" being similar
# is the same as "fine" and "great" being similar.
# 
# Also, a word is always similar with itself. For example, the sentences words1
# = ["great"], words2 = ["great"], pairs = [] are similar, even though there
# are no specified similar word pairs.
# 
# Finally, sentences can only be similar if they have the same number of words.
# So a sentence like words1 = ["great"] can never be similar to words2 =
# ["doubleplus","good"].
# 
# Note:
# 
# 
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
# 
# 
# 
# 
#
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
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

import itertools

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        # Depth-First Search
        # Time  complexity: O(N x P), where N is the maximum length of words1 and words2,
        # and P is the length of pairs. Each of N searches could search the entire graph.
        # Space compleixty: O(P), the size of pairs.
        # if len(words1) != len(words2): return False
        # graph = defaultdict(list)
        # for w1, w2 in pairs:
        #     graph[w1].append(w2)
        #     graph[w2].append(w1)

        # for w1, w2 in zip(words1, words2):
        #     stack, seen = [w1], {w1}
        #     while stack:
        #         word = stack.pop()
        #         if word == w2: break
        #         for nei in graph[word]:
        #             if not nei in seen:
        #                 seen.add(nei)
        #                 stack.append(nei)
        #     else:
        #         return False

        # return True


        # Union-Find
        # Time  complexity: O(NlogP + P), where N is the maximum length of words1 and words2,
        # and P is the length of pairs. If we use union-by-rank, this complexity improves to
        # O(N x a(P) + P) = O(N + P), where a is the Inverse-Ackermann function.
        # Space complexity: O(P), the size of pairs.
        if len(words1) != len(words2): return False

        index = {}
        count = itertools.count()
        dsu = DSU(2 * len(pairs))
        for pair in pairs:
            for p in pair:
                if p not in index:
                    index[p] = next(count)
            dsu.union(index[pair[0]], index[pair[1]])

        return all(w1 == w2 or w1 in index and w2 in index and 
                   dsu.find(index[w1]) == dsu.find(index[w2])
                   for w1, w2 in zip(words1, words2))

        
            



        

