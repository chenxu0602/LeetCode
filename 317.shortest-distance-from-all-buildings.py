#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#
# https://leetcode.com/problems/shortest-distance-from-all-buildings/description/
#
# algorithms
# Hard (37.86%)
# Likes:    444
# Dislikes: 24
# Total Accepted:    41.5K
# Total Submissions: 109.3K
# Testcase Example:  '[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# You want to build a house on an empty land which reaches all buildings in the
# shortest amount of distance. You can only move up, down, left and right. You
# are given a 2D grid of values 0, 1 or 2, where:
# 
# 
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# 
# 
# Example:
# 
# 
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# 
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 
# Output: 7 
# 
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at
# (0,2),
# ⁠            the point (1,2) is an ideal empty land to build a house, as the
# total 
# travel distance of 3+3+1=7 is minimal. So return 7.
# 
# Note:
# There will be at least one building. If it is not possible to build such
# house according to the above rules, return -1.
# 
#
from collections import defaultdict, deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        m, n, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
        hit, distSum = [[0] * n for i in range(m)], [[0] * n for i in range(m)]

        def bfs(x, y):
            visited = [[False] * n for k in range(m)]
            visited[x][y], count1, queue = True, 1, deque([(x, y, 0)])

            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= i < m and 0 <= j < n and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:
                            queue.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            return count1 == buildings

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    if not bfs(x, y):
                        return -1

        return min([distSum[i][j] for i in range(m) for j in range(n) if not grid[i][j] and hit[i][j] == buildings] or [-1])
        

