#
# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#
# https://leetcode.com/problems/regions-cut-by-slashes/description/
#
# algorithms
# Medium (62.91%)
# Likes:    389
# Dislikes: 85
# Total Accepted:    9.7K
# Total Submissions: 15.3K
# Testcase Example:  '[" /","/ "]'
#
# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /,
# \, or blank space.  These characters divide the square into contiguous
# regions.
# 
# (Note that backslash characters are escaped, so a \ is represented as "\\".)
# 
# Return the number of regions.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input:
# [
# " /",
# "/ "
# ]
# Output: 2
# Explanation: The 2x2 grid is as follows:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input:
# [
# " /",
# "  "
# ]
# Output: 1
# Explanation: The 2x2 grid is as follows:
# 
# 
# 
# 
# Example 3:
# 
# 
# Input:
# [
# "\\/",
# "/\\"
# ]
# Output: 4
# Explanation: (Recall that because \ characters are escaped, "\\/" refers to
# \/, and "/\\" refers to /\.)
# The 2x2 grid is as follows:
# 
# 
# 
# 
# Example 4:
# 
# 
# Input:
# [
# "/\\",
# "\\/"
# ]
# Output: 5
# Explanation: (Recall that because \ characters are escaped, "/\\" refers to
# /\, and "\\/" refers to \/.)
# The 2x2 grid is as follows:
# 
# 
# 
# 
# Example 5:
# 
# 
# Input:
# [
# "//",
# "/ "
# ]
# Output: 3
# Explanation: The 2x2 grid is as follows:
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] is either '/', '\', or ' '.
# 
# 
# 
# 
# 
# 
#
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
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                if r + 1 < N: dsu.union(root + 3, (root + 4*N) + 0)
                if r - 1 >= 0: dsu.union(root + 0, (root - 4*N) + 3)

                if c + 1 < N: dsu.union(root + 2, (root + 4) + 1)
                if c - 1 >= 0: dsu.union(root + 1, (root - 4) + 2)

        return sum(dsu.find(x) == x for x in range(4 * N * N))
        

