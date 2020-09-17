#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#
# https://leetcode.com/problems/spiral-matrix-iii/description/
#
# algorithms
# Medium (67.61%)
# Likes:    161
# Dislikes: 229
# Total Accepted:    15.9K
# Total Submissions: 23.5K
# Testcase Example:  '1\n4\n0\n0'
#
# On a 2 dimensional grid with R rows and C columns, we start at (r0, c0)
# facing east.
# 
# Here, the north-west corner of the grid is at the first row and column, and
# the south-east corner of the grid is at the last row and column.
# 
# Now, we walk in a clockwise spiral shape to visit every position in this
# grid. 
# 
# Whenever we would move outside the boundary of the grid, we continue our walk
# outside the grid (but may return to the grid boundary later.) 
# 
# Eventually, we reach all R * C spaces of the grid.
# 
# Return a list of coordinates representing the positions of the grid in the
# order they were visited.
# 
# 
# 
# Example 1:
# 
# 
# Input: R = 1, C = 4, r0 = 0, c0 = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
# 
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: R = 5, C = 6, r0 = 1, c0 = 4
# Output:
# [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
# 
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
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C
# 
# 
# 
#

# @lc code=start
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # Walk in a Spiral
        # Time  complexity: O(max(R, C)^2)
        # Space complexity: O(R x C)
        # ans = [(r0, c0)]
        # if R * C == 1: return ans

        # # For walk length k = 1, 3, 5 ...
        # for k in range(1, 2 * (R + C), 2):
        #     # For direction (dr, dc) = east, south, west, north;
        #     # and walk length dk ...
        #     for dr, dc, dk in (0, 1, k), (1, 0, k), (0, -1, k + 1), (-1, 0, k + 1):
        #         # For each of dk units in the current direction ...
        #         for _ in range(dk):
        #             r0 += dr
        #             c0 += dc

        #             # If on the grid ...
        #             if 0 <= r0 < R and 0 <= c0 < C:
        #                 ans.append((r0, c0))
        #                 if len(ans) == R * C:
        #                     return ans


        res = []
        dr, dc, n = 0, 1, 0
        while len(res) < R * C:
            for i in range(n // 2 + 1):
                if 0 <= r0 < R and 0 <= c0 < C:
                    res.append([r0, c0])
                r0, c0 = r0 + dr, c0 + dc
            dr, dc, n = dc, -dr, n + 1
        return res
        
# @lc code=end

