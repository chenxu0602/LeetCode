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
        self.par = list(range(N))
        self.rnk = [0] * N
        self.siz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr 
        self.siz[xr] += self.siz[yr]

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Time  complexity: O(N x N x a(N)) where a is the Inverse-Ackermann function (if we were to use union-find by rank.)
        # Space complexity: O(N x N)
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r * N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north / south
                if r + 1 < N: dsu.union(root + 3, (root + 4 * N) + 0)
                if r - 1 >= 0: dsu.union(root + 0, (root - 4 * N) + 3)
                # east / west
                if c + 1 < N: dsu.union(root + 2, (root + 4) + 1)
                if c - 1 >= 0: dsu.union(root + 1, (root - 4) + 2)

        return sum(dsu.find(x) == x for x in range(4 * N * N))
        

