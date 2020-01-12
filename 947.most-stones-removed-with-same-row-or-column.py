#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
#
# algorithms
# Medium (54.44%)
# Likes:    574
# Dislikes: 173
# Total Accepted:    30.8K
# Total Submissions: 56.3K
# Testcase Example:  '[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]'
#
# On a 2D plane, we place stones at some integer coordinate points.  Each
# coordinate point may have at most one stone.
# 
# Now, a move consists of removing a stone that shares a column or row with
# another stone on the grid.
# 
# What is the largest possible number of moves we can make?
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# 
# 
# 
# Example 2:
# 
# 
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: stones = [[0,0]]
# Output: 0
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= stones.length <= 1000
# 0 <= stones[i][j] < 10000
# 
# 
# 
# 
# 
#
from collections import defaultdict

class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        graph = defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1

        return ans
        """

        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y+10000)

        return N - len({dsu.find(x) for x, y in stones})

        

