#
# @lc app=leetcode id=1210 lang=python3
#
# [1210] Minimum Moves to Reach Target with Rotations
#
# https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/description/
#
# algorithms
# Hard (43.97%)
# Likes:    81
# Dislikes: 28
# Total Accepted:    3.8K
# Total Submissions: 8.6K
# Testcase Example:  '[[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]\r'
#
# In an n*n grid, there is a snake that spans 2 cells and starts moving from
# the top left corner at (0, 0) and (0, 1). The grid has empty cells
# represented by zeros and blocked cells represented by ones. The snake wants
# to reach the lower right corner at (n-1, n-2) and (n-1, n-1).
# 
# In one move the snake can:
# 
# 
# Move one cell to the right if there are no blocked cells there. This move
# keeps the horizontal/vertical position of the snake as it is.
# Move down one cell if there are no blocked cells there. This move keeps the
# horizontal/vertical position of the snake as it is.
# Rotate clockwise if it's in a horizontal position and the two cells under it
# are both empty. In that case the snake moves from (r, c) and (r, c+1) to (r,
# c) and (r+1, c).
# 
# Rotate counterclockwise if it's in a vertical position and the two cells to
# its right are both empty. In that case the snake moves from (r, c) and (r+1,
# c) to (r, c) and (r, c+1).
# 
# 
# 
# Return the minimum number of moves to reach the target.
# 
# If there is no way to reach the target, return -1.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid = [[0,0,0,0,0,1],
# ⁠              [1,1,0,0,1,0],
# [0,0,0,0,1,1],
# [0,0,1,0,1,0],
# [0,1,1,0,0,0],
# [0,1,1,0,0,0]]
# Output: 11
# Explanation:
# One possible solution is [right, right, rotate clockwise, right, down, down,
# down, down, rotate counterclockwise, right, down].
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,0,1,1,1,1],
# [0,0,0,0,1,1],
# [1,1,0,0,0,1],
# [1,1,1,0,0,1],
# [1,1,1,0,0,1],
# [1,1,1,0,0,0]]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 100
# 0 <= grid[i][j] <= 1
# It is guaranteed that the snake starts at empty cells.
# 
# 
#

# @lc code=start
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q, seen, target = [(0, 0, 0, 0)], set(), (n-1, n-2, 0)

        for r, c, dr, steps in q:
            if (r, c, dr) == target:
                return steps
            if (r, c, dr) not in seen:
                seen.add((r, c, dr))
                if dr:
                    if c+1 < n and grid[r][c+1] + grid[r+1][c+1] == 0:
                        q += [(r, c+1, 1, steps+1), (r, c, 0, steps+1)]
                    if r+2 < n and grid[r+2][c] == 0:
                        q += [(r+1, c, 1, steps+1)]
                else:
                    if r+1 < n and grid[r+1][c] + grid[r+1][c+1] == 0:
                        q += [(r+1, c, 0, steps+1), (r, c, 1, steps+1)]
                    if c+2 < n and grid[r][c+2] == 0:
                        q += [(r, c+1, 0, steps+1)]

        return -1
        
# @lc code=end

