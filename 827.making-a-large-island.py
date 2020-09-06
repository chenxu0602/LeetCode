#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#
# https://leetcode.com/problems/making-a-large-island/description/
#
# algorithms
# Hard (45.49%)
# Likes:    475
# Dislikes: 15
# Total Accepted:    19.4K
# Total Submissions: 42.1K
# Testcase Example:  '[[1,0],[0,1]]'
#
# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
# 
# After, what is the size of the largest island? (An island is a
# 4-directionally connected group of 1s).
# 
# Example 1:
# 
# 
# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with
# area = 3.
# 
# 
# Example 2:
# 
# 
# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island
# with area = 4.
# 
# Example 3:
# 
# 
# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
# 
# 
# 
# Notes:
# 
# 
# 1 <= grid.length = grid[0].length <= 50.
# 0 <= grid[i][j] <= 1.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Component Sizes
        # Time  complexity: O(N^2)
        # Space complexity: O(N^2)
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area, index = {}, 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])     
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))

        return ans
        
        
# @lc code=end

