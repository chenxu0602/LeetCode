#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#
# https://leetcode.com/problems/path-with-maximum-gold/description/
#
# algorithms
# Medium (63.12%)
# Likes:    250
# Dislikes: 11
# Total Accepted:    15.8K
# Total Submissions: 25.1K
# Testcase Example:  '[[0,6,0],[5,8,7],[0,9,0]]'
#
# In a gold mine grid of size m * n, each cell in this mine has an integer
# representing the amount of gold in that cell, 0 if it is empty.
# 
# Return the maximum amount of gold you can collect under the conditions:
# 
# 
# Every time you are located in a cell you will collect all the gold in that
# cell.
# From your position you can walk one step to the left, right, up or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has
# some gold.
# 
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
# ⁠[5,8,7],
# ⁠[0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
# ⁠[2,0,6],
# ⁠[3,4,5],
# ⁠[0,3,0],
# ⁠[9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length, grid[i].length <= 15
# 0 <= grid[i][j] <= 100
# There are at most 25 cells containing gold.
# 
#

# @lc code=start
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # BFS
        m, n, q, goldCellId, ans = len(grid), len(grid[0]), [], 0, 0
        oneCellTrace = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    oneCellTrace[i][j] = 1 << goldCellId
                    goldCellId += 1
                    q.append((i, j, grid[i][j], oneCellTrace[i][j]))

        for i, j, s, trace in q:
            ans = max(ans, s)
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                r, c = i+dr, j+dc
                if 0 <= r < m and 0 <= c < n and grid[r][c] and not(trace & oneCellTrace[r][c]):
                    q.append((r, c, grid[r][c] + s, trace | oneCellTrace[r][c]))

        return ans
                

        
# @lc code=end

