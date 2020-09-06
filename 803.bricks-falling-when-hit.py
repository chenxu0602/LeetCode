#
# @lc app=leetcode id=803 lang=python3
#
# [803] Bricks Falling When Hit
#
# https://leetcode.com/problems/bricks-falling-when-hit/description/
#
# algorithms
# Hard (30.68%)
# Likes:    459
# Dislikes: 134
# Total Accepted:    15.9K
# Total Submissions: 51.3K
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

# @lc code=start
class DSU:
    def __init__(self, R, C):
        # R * C is the source, and isn't a grid square
        self.par = list(range(R * C + 1))
        self.rnk = [0] * (R * C + 1)
        self.siz = [1] * (R * C + 1)

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

    def size(self, x):
        return self.siz[self.find(x)]

    def top(self):
        # Size of component at ephemeral "source" node at index R * C,
        # minus 1 to not count the source itself in the size
        return self.size(len(self.siz) - 1) - 1

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # Reverse Time and Union-Find
        # Time  complexity: O(N x Q x a(N x Q)), where N = R x C is the number of grid squares,
        # Q is the length of hits, and a is the Inverse-Ackermann function.
        # Space complexity: O(N)
        R, C = map(len, (grid, grid[0]))
        def index(r, c): return r * C + c

        def neighbors(r, c):
            for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
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
                        dsu.union(i, R * C)
                    if r and A[r - 1][c]:
                        dsu.union(i, index(r - 1, c))
                    if c and A[r][c - 1]:
                        dsu.union(i, index(r, c - 1))

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
                    dsu.union(i, R * C)
                A[r][c] = 1
                ans.append(max(0, dsu.top() - pre_roof - 1))

        return ans[::-1]

        
# @lc code=end

