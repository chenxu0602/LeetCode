#
# @lc app=leetcode id=694 lang=python3
#
# [694] Number of Distinct Islands
#
# https://leetcode.com/problems/number-of-distinct-islands/description/
#
# algorithms
# Medium (54.15%)
# Likes:    588
# Dislikes: 40
# Total Accepted:    42.6K
# Total Submissions: 78.5K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
# 
# Count the number of distinct islands.  An island is considered to be the same
# as another if and only if one island can be translated (and not rotated or
# reflected) to equal the other.
# 
# Example 1:
# 
# 11000
# 11000
# 00011
# 00011
# 
# Given the above grid map, return 1.
# 
# 
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
# Notice that:
# 
# 11
# 1
# 
# and
# 
# ⁠1
# 11
# 
# are considered different island shapes, because we do not consider reflection
# / rotation.
# 
# 
# Note:
# The length of each dimension in the given grid does not exceed 50.
# 
#

# @lc code=start
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        seen = set()

        def explore(r, c, r0, c0):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] and (r, c) not in seen:
                seen.add((r, c))
                shape.add((r - r0, c - c0))
                explore(r+1, c, r0, c0)
                explore(r-1, c, r0, c0)
                explore(r, c+1, r0, c0)
                explore(r, c-1, r0, c0)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c, r, c)
                if shape:
                    shapes.add(frozenset(shape))
        return len(shapes)
        
# @lc code=end

