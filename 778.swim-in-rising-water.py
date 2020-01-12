#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#
# https://leetcode.com/problems/swim-in-rising-water/description/
#
# algorithms
# Hard (48.61%)
# Likes:    339
# Dislikes: 32
# Total Accepted:    14.2K
# Total Submissions: 29.2K
# Testcase Example:  '[[0,2],[1,3]]'
#
# On an N x N grid, each square grid[i][j] represents the elevation at that
# point (i,j).
# 
# Now rain starts to fall. At time t, the depth of the water everywhere is t.
# You can swim from a square to another 4-directionally adjacent square if and
# only if the elevation of both squares individually are at most t. You can
# swim infinite distance in zero time. Of course, you must stay within the
# boundaries of the grid during your swim.
# 
# You start at the top left square (0, 0). What is the least time until you can
# reach the bottom right square (N-1, N-1)?
# 
# Example 1:
# 
# 
# Input: [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a
# higher elevation than t = 0.
# 
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
# 
# 
# Example 2:
# 
# 
# Input:
# [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation:
# ⁠0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6
# 
# The final route is marked in bold.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
# 
# 
# Note:
# 
# 
# 2 <= N <= 50.
# grid[i][j] is a permutation of [0, ..., N*N - 1].
# 
# 
#
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        seen = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]
        ans = 0

        while pq:
            d, r, c = heapq.heappop(pq)
            ans = max(ans, d)
            if r == c == N-1: return ans
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen:
                    heapq.heappush(pq, (grid[cr][cc], cr, cc))
                    seen.add((cr, cc))

        """
        N = len(grid)
        l, r = 2*N-2, N*N

        def search(i, j):
            if ele[i][j]:
                return False
            ele[i][j] = 1
            if grid[i][j] <= ans:
                if i == j == N - 1:
                    return True
                return any([search(a, b) for a, b in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0 <= a < N and 0 <= b < N])

        for ans in range(max(l, grid[-1][-1]), r):
            ele = [[0] * N for _ in range(N)]
            if search(0, 0):
                return ans
        """

        

