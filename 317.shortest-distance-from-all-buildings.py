#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#
# https://leetcode.com/problems/shortest-distance-from-all-buildings/description/
#
# algorithms
# Hard (41.31%)
# Likes:    799
# Dislikes: 48
# Total Accepted:    70.6K
# Total Submissions: 170.4K
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

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # BFS with pruning
        # O((M x N)^2)
        if not grid:
            return -1

        m, n = map(len, (grid, grid[0]))
        buildings = sum(val for line in grid for val in line if val == 1)
        hits    = [[0] * n for _ in range(m)]
        distSum = [[0] * n for _ in range(m)]

        def bfs(p, q):
            visited = [[False] * n for _ in range(m)]
            visited[p][q] = True

            count1 = 1
            queue = deque([(p, q, 0)])

            while queue:
                x, y, dist = queue.popleft()
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        if not grid[nx][ny]:
                            queue.append((nx, ny, dist + 1))
                            hits[nx][ny] += 1
                            distSum[nx][ny] += dist + 1
                        elif grid[nx][ny] == 1:
                            count1 += 1
                        
            return count1 == buildings


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1

        return min([distSum[i][j] for i in range(m) for j in range(n) if not grid[i][j] and hits[i][j] == buildings] or [-1])
        
# @lc code=end

