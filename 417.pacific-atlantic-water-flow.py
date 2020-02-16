#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (39.26%)
# Likes:    952
# Dislikes: 177
# Total Accepted:    61.1K
# Total Submissions: 155.5K
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

# @lc code=start
from collections import deque

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        if not matrix: return []
        m, n = len(matrix), len(matrix[0])

        def bfs(reachable_ocean):
            queue = deque(reachable_ocean)
            while queue:
                (i, j) = queue.popleft()
                for (di, dj) in (0, 1), (0, -1), (1, 0), (-1, 0):
                    if 0 <= i + di < m and 0 <= j + dj < n \
                        and (i + di, j + dj) not in reachable_ocean \
                        and matrix[i+di][j+dj] >= matrix[i][j]:
                        queue.append((i + di, j + dj))
                        reachable_ocean.add((i + di, j + dj))
            return reachable_ocean

        pacific = set([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)]) 
        atlantic = set([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)])
        return list(bfs(pacific) & bfs(atlantic))


        
# @lc code=end

