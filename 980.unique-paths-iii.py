#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
# https://leetcode.com/problems/unique-paths-iii/description/
#
# algorithms
# Hard (73.22%)
# Likes:    999
# Dislikes: 80
# Total Accepted:    54.5K
# Total Submissions: 70.9K
# Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
#
# On a 2-dimensional grid, there are 4 types of squares:
# 
# 
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# 
# 
# Return the number of 4-directional walks from the starting square to the
# ending square, that walk over every non-obstacle square exactly once.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# 
# 
# Example 2:
# 
# 
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# 
# 
# Example 3:
# 
# 
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length * grid[0].length <= 20
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        # R, C = map(len, (grid, grid[0]))

        # def neighbors(r, c):
        #     for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        #         if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
        #             yield nr, nc

        # todo = 0
        # for r, row in enumerate(grid):
        #     for c, val in enumerate(row):
        #         if val != -1: todo += 1
        #         if val == 1: sr, sc = r, c
        #         if val == 2: tr, tc = r, c

        # self.ans = 0
        # def dfs(r, c, todo):
        #     todo -= 1
        #     if todo < 0: return
        #     if r == tr and c == tc:
        #         if todo == 0:
        #             self.ans += 1
        #         return

        #     grid[r][c] = -1
        #     for nr, nc in neighbors(r, c):
        #         dfs(nr, nc, todo)
        #     grid[r][c] = 0

        # dfs(sr, sc, todo)
        # return self.ans


        # R, C = map(len, (grid, grid[0]))
        
        # def code(r, c):
        #     return 1 << (r * C + c)

        # def neighbors(r, c):
        #     for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        #         if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
        #             yield nr, nc

        # target = 0
        # for r, row in enumerate(grid):
        #     for c, val in enumerate(row):
        #         if val % 2 == 0:
        #             target |= code(r, c)

        #         if val == 1:
        #             sr, sc = r, c
                
        #         if val == 2:
        #             tr, tc = r, c

        # @lru_cache(None)
        # def dp(r, c, todo):
        #     if r == tr and c == tc:
        #         return +(todo == 0)
        #     ans = 0
        #     for nr, nc in neighbors(r, c):
        #         if todo & code(nr, nc):
        #             ans += dp(nr, nc, todo ^ code(nr, nc))
        #     return ans

        # return dp(sr, sc, target)


        # Time  complexity: O(3 ^ N)
        # Although technically we have 4 directions to explore at each step, we have at most 3 directions to try at any moment except the first step. The last direction is the direction where we came from, therefore we don't need to explore it, since we have been there before.
        # In the worst case where none of the cells is an obstacle, we have to explore each cell. Hence, the time complexity of the algorithm is O(4 x 3^(N-1)) = O(3^N).
        # Space complexity: O(N), we apply recursion in the algorithm, which could incur O(N) space in the function call stack.


        R, C = map(len, (grid, grid[0]))
        cnt, flat = 0, sum(grid, [])

        def dfs(r, c, left):
            nonlocal cnt
            grid[r][c] = -1
            for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= nr < R and 0 <= nc < C:
                    if not grid[nr][nc]:
                        dfs(nr, nc, left - 1)
                    if grid[nr][nc] == 2:
                        cnt += not left
            grid[r][c] = 0

        dfs(*divmod(flat.index(1), C), flat.count(0))
        return cnt
        
# @lc code=end

