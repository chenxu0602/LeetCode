#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (37.65%)
# Likes:    687
# Dislikes: 112
# Total Accepted:    45.6K
# Total Submissions: 121.1K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# 
# 
# Example:
# 
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
# 
# 
#

from collections import deque

class Solution:
    def dfs(self, matrix, i, j, visited, m, n):
        visited[i][j] = True
        for d in self.directions:
            x, y = i + d[0], j + d[1]
            if x < 0 or x >= m or y < 0 or y >= n \
                or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        """
        if not matrix: return []
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        m, n = len(matrix), len(matrix[0])

        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []

        for i in range(m):
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n-1, a_visited, m, n)

        for j in range(n):
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m-1, j, a_visited, m, n)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i, j])

        return result
        """

        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        def bfs(reachable_ocean):
            queue = deque(reachable_ocean)
            while queue:
                (i, j) = queue.popleft()
                for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= i + di < m and 0 <= j + dj < n \
                        and (i + di, j + dj) not in reachable_ocean \
                        and matrix[i + di][j + dj] >= matrix[i][j]:
                        queue.append((i + di, j + dj))
                        reachable_ocean.add((i + di, j + dj))
            return reachable_ocean


        pacific = set([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)])
        atlantic = set([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)])
        return list(bfs(pacific) & bfs(atlantic))
        

