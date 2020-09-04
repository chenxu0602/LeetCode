#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#
# https://leetcode.com/problems/swim-in-rising-water/description/
#
# algorithms
# Hard (50.53%)
# Likes:    454
# Dislikes: 38
# Total Accepted:    19.1K
# Total Submissions: 37.6K
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

# @lc code=start
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Heap
        # Time  complexity: O(N^2 x logN)
        # Space complexity: O(N^2)
        N, seen, ans = len(grid), {(0, 0)}, 0
        pq = [(grid[0][0], 0, 0)]
        while pq:
            d, r, c = heapq.heappop(pq)
            ans = max(ans, d)
            if r == c == N - 1: return ans
            for cr, cc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen:
                    heapq.heappush(pq, (grid[cr][cc], cr, cc))
                    seen.add((cr, cc))


        # Binary Search and DFS
        # Time  complexity: O(N^2 x logN)
        # Space complexity: O(N^2)
        # def possible(T):
        #     stack, seen = [(0, 0)], {(0, 0)}
        #     while stack:
        #         r, c = stack.pop()
        #         if r == c == N - 1: return True
        #         for cr, cc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        #             if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen and grid[cr][cc] <= T:
        #                 stack.append((cr, cc))
        #                 seen.add((cr, cc))
        #     return False

        # N = len(grid)
        # lo, hi = grid[0][0], N * N
        # while lo < hi:
        #     mi = (lo + hi) // 2
        #     if not possible(mi):
        #         lo = mi + 1
        #     else:
        #         hi = mi
        # return lo
        
# @lc code=end

