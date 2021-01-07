#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#
# https://leetcode.com/problems/where-will-the-ball-fall/description/
#
# algorithms
# Medium (57.59%)
# Likes:    141
# Dislikes: 16
# Total Accepted:    5.4K
# Total Submissions: 9.4K
# Testcase Example:  '[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]'
#
# You have a 2-D grid of size m x n representing a box, and you have n balls.
# The box is open on the top and bottom sides.
# 
# Each cell in the box has a diagonal board spanning two corners of the cell
# that can redirect a ball to the right or to the left.
# 
# 
# A board that redirects the ball to the right spans the top-left corner to the
# bottom-right corner and is represented in the grid as 1.
# A board that redirects the ball to the left spans the top-right corner to the
# bottom-left corner and is represented in the grid as -1.
# 
# 
# We drop one ball at the top of each column of the box. Each ball can get
# stuck in the box or fall out of the bottom. A ball gets stuck if it hits a
# "V" shaped pattern between two boards or if a board redirects the ball into
# either wall of the box.
# 
# Return an array answer of size n where answer[i] is the column that the ball
# falls out of at the bottom after dropping the ball from the i^th column at
# the top, or -1 if the ball gets stuck in the box.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid =
# [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
# Output: [1,-1,-1,-1,-1]
# Explanation: This example is shown in the photo.
# Ball b0 is dropped at column 0 and falls out of the box at column 1.
# Ball b1 is dropped at column 1 and will get stuck in the box between column 2
# and 3 and row 1.
# Ball b2 is dropped at column 2 and will get stuck on the box between column 2
# and 3 and row 0.
# Ball b3 is dropped at column 3 and will get stuck on the box between column 2
# and 3 and row 0.
# Ball b4 is dropped at column 4 and will get stuck on the box between column 2
# and 3 and row 1.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[-1]]
# Output: [-1]
# Explanation: The ball gets stuck against the left wall.
# 
# 
# Example 3:
# 
# 
# Input: grid =
# [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
# Output: [0,1,2,3,4,-1]
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is 1 or -1.
# 
# 
#

# @lc code=start
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # We drop the ball at grid[0][i] and track ball position i1, which initlized as i.
        # An observation is that, if the ball wants to move from i1 to i2,
        # we must have the board direction grid[j][i1] == grid[j][i2]
        # Time  complexity: O(mn)
        # Space complexity: O(n)
        m, n = map(len, (grid, grid[0]))

        def test(i):
            for j in range(m):
                i2 = i + grid[j][i]
                if i2 < 0 or i2 >= n or grid[j][i2] != grid[j][i]:
                    return -1
                i = i2
            return i

        return map(test, range(n))
        
# @lc code=end

