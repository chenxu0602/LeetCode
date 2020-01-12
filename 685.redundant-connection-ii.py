#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#
# https://leetcode.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (30.92%)
# Likes:    488
# Dislikes: 159
# Total Accepted:    24.4K
# Total Submissions: 78.6K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 
# In this problem, a rooted tree is a directed graph such that, there is
# exactly one node (the root) for which all other nodes are descendants of this
# node, plus every node has exactly one parent, except for the root node which
# has no parents.
# 
# The given input is a directed graph that started as a rooted tree with N
# nodes (with distinct values 1, 2, ..., N), with one additional directed edge
# added.  The added edge has two different vertices chosen from 1 to N, and was
# not an edge that already existed.
# 
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] that represents a directed edge connecting nodes u and v,
# where u is a parent of child v.
# 
# Return an edge that can be removed so that the resulting graph is a rooted
# tree of N nodes.  If there are multiple answers, return the answer that
# occurs last in the given 2D-array.
# Example 1:
# 
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
# 
# 
# Example 2:
# 
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5  2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4 
# 
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
# 
#
class DSU:
    def __init__(self, N):
        self.ranks = [0] * (N+1)
        self.groups = list(range(N+1))
        
    def find(self, x):
        if self.groups[x] == x:
            return x
        return self.find(self.groups[x])
    
    def union(self, x, y):
        gx = self.find(x)
        gy = self.find(y)
        if gx == gy: 
            return False
        if self.ranks[gx] > self.ranks[gy]:
            self.groups[gy] = gx
        elif self.ranks[gx] < self.ranks[gy]:
            self.groups[gx] = gy
        else:
            self.groups[gy] = gx
            self.ranks[gy] += 1
        return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        def is_cycle(edge):
            """
                return True if from edge=x, y can get back to x
            """
            x, y = edge
            while x != y and x in parent:
                x = parent[x]
            return x == y
            
        parent = {}
        candidates = []
        for x, y in edges:
            if y not in parent:
                parent[y] = x
            else:
                candidates.append([parent[y], y])
                candidates.append([x, y])
                
        if candidates:
            if is_cycle(candidates[0]):
                return candidates[0]
            return candidates[1]
            
        else:
            N = len(edges)
            dsu = DSU(N)
            for x, y in edges:
                if not dsu.union(x, y):
                    return [x, y]
        return []

