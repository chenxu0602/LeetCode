#
# @lc app=leetcode id=1391 lang=python3
#
# [1391] Check if There is a Valid Path in a Grid
#
# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description/
#
# algorithms
# Medium (44.80%)
# Likes:    250
# Dislikes: 151
# Total Accepted:    12K
# Total Submissions: 26.8K
# Testcase Example:  '[[2,4,3],[6,5,2]]'
#
# Given a m x n grid. Each cell of the grid represents a street. The street of
# grid[i][j] can be:
# 
# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.
# 
# 
# 
# 
# You will initially start at the street of the upper-left cell (0,0). A valid
# path in the grid is a path which starts from the upper left cell (0,0) and
# ends at the bottom-right cell (m - 1, n - 1). The path should only follow the
# streets.
# 
# Notice that you are not allowed to change any street.
# 
# Return true if there is a valid path in the grid or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[2,4,3],[6,5,2]]
# Output: true
# Explanation: As shown you can start at cell (0, 0) and visit all the cells of
# the grid to reach (m - 1, n - 1).
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,2,1],[1,2,1]]
# Output: false
# Explanation: As shown you the street at cell (0, 0) is not connected with any
# street of any other cell and you will get stuck at cell (0, 0)
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,1,2]]
# Output: false
# Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0,
# 2).
# 
# 
# Example 4:
# 
# 
# Input: grid = [[1,1,1,1,1,1,3]]
# Output: true
# 
# 
# Example 5:
# 
# 
# Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# 1 <= grid[i][j] <= 6
# 
# 
#

# @lc code=start
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = map(len, (grid, grid[0]))
        uf = {(i, j): (i, j) for i in range(-1, 2 * m) for j in range(-1, 2 * n)}

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def merge(i, j, di, dj):
            uf[find((i, j))] = find((i + di, j + dj))

        for i in range(m):
            for j in range(n):
                if grid[i][j] in [2, 5, 6]: merge(2 * i, 2 * j, -1, 0)
                if grid[i][j] in [1, 3, 5]: merge(2 * i, 2 * j, 0, -1)
                if grid[i][j] in [2, 3, 4]: merge(2 * i, 2 * j, 1, 0)
                if grid[i][j] in [1, 4, 6]: merge(2 * i, 2 * j, 0, 1)

        return find((0, 0)) == find((2 * m - 2, 2 * n -2))
        
# @lc code=end

