#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
#
# algorithms
# Hard (40.81%)
# Likes:    201
# Dislikes: 2
# Total Accepted:    5.6K
# Total Submissions: 13.7K
# Testcase Example:  '[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1'
#
# Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In
# one step, you can move up, down, left or right from and to an empty cell.
# 
# Return the minimum number of steps to walk from the upper left corner (0, 0)
# to the lower right corner (m-1, n-1) given that you can eliminate at most k
# obstacles. If it is not possible to find such walk return -1.
# 
# 
# Example 1:
# 
# 
# Input: 
# grid = 
# [[0,0,0],
# [1,1,0],
# ⁠[0,0,0],
# [0,1,1],
# ⁠[0,0,0]], 
# k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10. 
# The shortest path with one obstacle elimination at position (3,2) is 6. Such
# path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# grid = 
# [[0,1,1],
# [1,1,1],
# [1,0,0]], 
# k = 1
# Output: -1
# Explanation: 
# We need to eliminate at least two obstacles to find such a walk.
# 
# 
# 
# Constraints:
# 
# 
# grid.length == m
# grid[0].length == n
# 1 <= m, n <= 40
# 1 <= k <= m*n
# grid[i][j] == 0 or 1
# grid[0][0] == grid[m-1][n-1] == 0
# 
#

# @lc code=start
import heapq
from collections import defaultdict, deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        # m, n = len(grid), len(grid[0])
        # q = deque([(0, 0, 0)])
        # visited = {(0, 0): 0}
        # steps = 0

        # while q:
        #     size = len(q)
        #     for _ in range(size):
        #         r, c, obs = q.popleft()
        #         if obs > k: continue
        #         if r == m - 1 and c == n - 1:
        #             return steps
        #         for r2, c2 in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
        #             if 0 <= r2 < m and 0 <= c2 < n:
        #                 next_obs = obs + 1 if grid[r2][c2] == 1 else obs
        #                 if next_obs < visited.get((r2, c2), float("inf")):
        #                     visited[(r2, c2)] = next_obs
        #                     q.append((r2, c2, next_obs))

        #     steps += 1

        # return -1

        m, n = len(grid), len(grid[0])
        if m + n - 2 <= k:
            return m + n - 2

        manhattan_distance = lambda y, x: m + n - y - x - 2
        neighborhood = lambda y, x: [
            (y, x) for y, x in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]
            if 0 <= y < m and 0 <= x < n
        ]

        fringe_heap = [(manhattan_distance(0, 0), 0, 0, 0, 0)]
        min_eliminations = defaultdict(lambda: k + 1, {(0, 0): 0})

        while fringe_heap:
            estimation, steps, eleminations, y, x = heapq.heappop(fringe_heap)

            if estimation - steps <= k - eleminations:
                return estimation

            for y, x in neighborhood(y, x):
                next_eliminations = eleminations + grid[y][x]

                if next_eliminations < min_eliminations[(y, x)]:
                    heapq.heappush(fringe_heap, (steps + 1 + manhattan_distance(y, x), steps + 1, next_eliminations, y, x))
                    min_eliminations[(y, x)] = next_eliminations

        return -1

        
# @lc code=end

