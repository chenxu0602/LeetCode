#
# @lc app=leetcode id=803 lang=python3
#
# [803] Bricks Falling When Hit
#
# https://leetcode.com/problems/bricks-falling-when-hit/description/
#
# algorithms
# Hard (29.09%)
# Likes:    325
# Dislikes: 96
# Total Accepted:    11.4K
# Total Submissions: 39.1K
# Testcase Example:  '[[1,0,0,0],[1,1,1,0]]\n[[1,0]]'
#
# We have a grid of 1s and 0s; the 1s in a cell represent bricks.  A brick will
# not drop if and only if it is directly connected to the top of the grid, or
# at least one of its (4-way) adjacent bricks will not drop.
# 
# We will do some erasures sequentially. Each time we want to do the erasure at
# the location (i, j), the brick (if it exists) on that location will
# disappear, and then some other bricks may drop because of that erasure.
# 
# Return an array representing the number of bricks that will drop after each
# erasure in sequence.
# 
# 
# Example 1:
# Input: 
# grid = [[1,0,0,0],[1,1,1,0]]
# hits = [[1,0]]
# Output: [2]
# Explanation: 
# If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So
# we should return 2.
# 
# 
# Example 2:
# Input: 
# grid = [[1,0,0,0],[1,1,0,0]]
# hits = [[1,1],[1,0]]
# Output: [0,0]
# Explanation: 
# When we erase the brick at (1, 0), the brick at (1, 1) has already
# disappeared due to the last move. So each erasure will cause no bricks
# dropping.  Note that the erased brick (1, 0) will not be counted as a dropped
# brick.
# 
# 
# 
# Note:
# 
# 
# The number of rows and columns in the grid will be in the range [1, 200].
# The number of erasures will not exceed the area of the grid.
# It is guaranteed that each erasure will be different from any other erasure,
# and located inside the grid.
# An erasure may refer to a location with no brick - if it does, no bricks
# drop.
# 
# 
#
class DSU:
    def __init__(self, R, C):
        self.param = list(range(R*C+1))
        self.ranks = [0] * (R*C + 1) 
        self.sizes = [1] * (R*C + 1)

    def find(self, x):
        if self.param[x] != x:
            self.param[x] = self.find(self.param[x])
        return self.param[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        if self.ranks[xr] < self.ranks[yr]:
            xr, yr = yr, xr
        if self.ranks[xr] == self.ranks[yr]:
            self.ranks[xr] += 1

        self.param[yr] = xr
        self.sizes[xr] += self.sizes[yr]

    def size(self, x):
        return self.sizes[self.find(x)]

    def top(self):
        return self.size(len(self.sizes) - 1) - 1

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:

        R, C = len(grid), len(grid[0])
        def index(r, c):
            return r * C + c

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        A = [row[:] for row in grid]
        for i, j in hits:
            A[i][j] = 0

        dsu = DSU(R, C)
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val:
                    i = index(r, c)
                    if r == 0:
                        dsu.union(i, R*C)
                    if r and A[r-1][c]:
                        dsu.union(i, index(r-1, c))
                    if c and A[r][c-1]:
                        dsu.union(i, index(r, c-1))

        ans = []
        for r, c in reversed(hits):
            pre_roof = dsu.top()
            if grid[r][c] == 0:
                ans.append(0)
            else:
                i = index(r, c)
                for nr, nc in neighbors(r, c):
                    if A[nr][nc]:
                        dsu.union(i, index(nr, nc))
                if r == 0:
                    dsu.union(i, R*C)
                A[r][c] = 1
                ans.append(max(0, dsu.top() - pre_roof - 1))
        return ans[::-1]

        

