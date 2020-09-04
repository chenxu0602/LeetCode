#
# @lc app=leetcode id=741 lang=python3
#
# [741] Cherry Pickup
#
# https://leetcode.com/problems/cherry-pickup/description/
#
# algorithms
# Hard (33.82%)
# Likes:    1088
# Dislikes: 79
# Total Accepted:    26.8K
# Total Submissions: 79K
# Testcase Example:  '[[0,1,-1],[1,0,-1],[1,1,1]]'
#
# In a N x N grid representing a field of cherries, each cell is one of three
# possible integers.
# 
# 
# 
# 
# 0 means the cell is empty, so you can pass through;
# 1 means the cell contains a cherry, that you can pick up and pass
# through;
# -1 means the cell contains a thorn that blocks your way.
# 
# 
# 
# 
# Your task is to collect maximum number of cherries possible by following the
# rules below:
# 
# 
# 
# 
# Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or
# down through valid path cells (cells with value 0 or 1);
# After reaching (N-1, N-1), returning to (0, 0) by moving left or up through
# valid path cells;
# When passing through a path cell containing a cherry, you pick it up and the
# cell becomes an empty cell (0);
# If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can
# be collected.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: grid =
# [[0, 1, -1],
# ⁠[1, 0, -1],
# ⁠[1, 1,  1]]
# Output: 5
# Explanation: 
# The player started at (0, 0) and went down, down, right right to reach (2,
# 2).
# 4 cherries were picked up during this single trip, and the matrix becomes
# [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more
# cherry.
# The total number of cherries picked up is 5, and this is the maximum
# possible.
# 
# 
# 
# 
# Note:
# 
# 
# grid is an N by N 2D array, with 1 <= N <= 50.
# Each grid[i][j] is an integer in the set {-1, 0, 1}.
# It is guaranteed that grid[0][0] and grid[N-1][N-1] are not
# -1.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Dynamic Programming (Top Down)
        # Time  complexity: O(N^3)
        # Space complexity: O(N^3)
        N = len(grid)
        memo = [[[None] * N for _1 in range(N)] for _2 in range(N)]
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if N == r1 or N == r2 or N == c1 or N == c2 or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")
            elif r1 == c1 == N - 1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                ans += max(dp(r1, c1 + 1, c2 + 1), dp(r1 + 1, c1, c2 + 1),
                           dp(r1, c1 + 1, c2), dp(r1 + 1, c1, c2))

                memo[r1][c1][c2] = ans
                return ans

        return max(0, dp(0, 0, 0))


        # Dynamic Programming (Bottom Up) 
        # Time  complexity: O(N^3)
        # Space complexity: O(N^2)
        # N = len(grid)
        # dp = [[float("-inf")] * N for _ in range(N)]
        # dp[0][0] = grid[0][0]
        # for t in range(1, 2 * N - 1):
        #     dp2 = [[float("-inf")] * N for _ in range(N)]
        #     for i in range(max(0, t - (N - 1)), min(N - 1, t) + 1):
        #         for j in range(max(0, t - (N - 1)), min(N - 1, t) + 1):
        #             if grid[i][t - i] == -1 or grid[j][t - j] == -1:
        #                 continue
        #             val = grid[i][t - i]
        #             if i != j: val += grid[j][t - j]
        #             dp2[i][j] = max(dp[pi][pj] + val
        #                             for pi in (i - 1, i) for pj in (j - 1, j)
        #                             if pi >= 0 and pj >= 0)

        #     dp = dp2
        # return max(0, dp[N - 1][N - 1])


        
# @lc code=end

