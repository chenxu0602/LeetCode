#
# @lc app=leetcode id=1559 lang=python3
#
# [1559] Detect Cycles in 2D Grid
#
# https://leetcode.com/problems/detect-cycles-in-2d-grid/description/
#
# algorithms
# Hard (44.67%)
# Likes:    206
# Dislikes: 6
# Total Accepted:    7.8K
# Total Submissions: 17.5K
# Testcase Example:  '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]'
#
# Given a 2D array of characters grid of size m x n, you need to find if there
# exists any cycle consisting of the same value in grid.
# 
# A cycle is a path of length 4 or more in the grid that starts and ends at the
# same cell. From a given cell, you can move to one of the cells adjacent to it
# - in one of the four directions (up, down, left, or right), if it has the
# same value of the current cell.
# 
# Also, you cannot move to the cell that you visited in your last move. For
# example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2)
# we visited (1, 1) which was the last visited cell.
# 
# Return true if any cycle of the same value exists in grid, otherwise, return
# false.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid =
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true
# Explanation: There are two valid cycles shown in different colors in the
# image below:
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: grid =
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# Explanation: There is only one valid cycle highlighted in the image below:
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 500
# 1 <= n <= 500
# grid consists only of lowercase English letters.
# 
# 
#
# @lc code=start
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
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        return True

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # Simple DFS
        # O(m x n)
        # def dfs(node, parent):
        #     if node in visited:
        #         return True

        #     visited.add(node)

        #     i, j = node
        #     for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
        #         if 0 <= x < m and 0 <= y < n and grid[x][y] == grid[i][j] \
        #             and (x, y) != parent:
        #             if dfs((x, y), node):
        #                 return True

        #     return False

        # m, n = map(len, (grid, grid[0]))
        # visited = set()
        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) in visited:
        #             continue
        #         if dfs((i, j), None):
        #             return True

        # return False


        # Once we found a cell is equal to its up and left cell, check their parents.
        # If parents of up and left cells are in the same union, it means there must be a cycle.
        # Time: O(MN)
        # Because we do path compression on find and union by rank on union, these two functions'         #        time complexity are both almost O(1)
        # Space: O(MN)
        m, n = map(len, (grid, grid[0]))

        def get_index(i, j):
            return i * n + j

        dsu = DSU(m * n)
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i > 0 and j > 0 and grid[i - 1][j] == grid[i][j - 1] == val \
                    and dsu.find(get_index(i - 1, j)) == dsu.find(get_index(i, j - 1)):
                    return True

                for r, c in (i - 1, j), (i, j - 1):
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == val:
                        dsu.union(i * n + j, r * n + c)

        return False
# @lc code=end

