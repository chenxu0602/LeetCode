#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#
# https://leetcode.com/problems/number-of-islands-ii/description/
#
# algorithms
# Hard (40.57%)
# Likes:    705
# Dislikes: 15
# Total Accepted:    67.8K
# Total Submissions: 167.2K
# Testcase Example:  '3\n3\n[[0,0],[0,1],[1,2],[2,1]]'
#
# A 2d grid map of m rows and n columns is initially filled with water. We may
# perform an addLand operation which turns the water at position (row, col)
# into a land. Given a list of positions to operate, count the number of
# islands after each addLand operation. An island is surrounded by water and is
# formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.
# 
# Example:
# 
# 
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# 
# 
# Explanation:
# 
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water
# and 1 represents land).
# 
# 
# 0 0 0
# 0 0 0
# 0 0 0
# 
# 
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
# 
# 
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# 
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
# 
# 
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# 
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
# 
# 
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# 
# 
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
# 
# 
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# 
# 
# Follow up:
# 
# Can you do it in time complexity O(k log mn), where k is the length of the
# positions?
# 
#

# @lc code=start
class Union:
    def __init__(self):
        self.par = {}
        self.rnk = {}
        self.siz = {}
        self.count = 0

    def add(self, p):
        self.par[p] = p
        self.rnk[p] = 0
        self.siz[p] = 1
        self.count += 1

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.siz[xr] += self.siz[yr]
        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        # Union Find (aka Disjoint Set)
        # Time  complexity: O(m x n + L)
        # Space complexity: O(m x n)
        ans, islands = [], Union()
        for x, y in positions:
            if (x, y) in islands.par:
                ans += ans[-1],
                continue

            islands.add((x, y))
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                nx, ny = x + dx, y + dy
                if (nx, ny) in islands.par:
                    islands.unite((x, y), (nx, ny))

            ans += islands.count,

        return ans
        
# @lc code=end

