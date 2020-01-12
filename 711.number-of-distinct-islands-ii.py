#
# @lc app=leetcode id=711 lang=python3
#
# [711] Number of Distinct Islands II
#
# https://leetcode.com/problems/number-of-distinct-islands-ii/description/
#
# algorithms
# Hard (46.43%)
# Likes:    101
# Dislikes: 115
# Total Accepted:    4.1K
# Total Submissions: 8.8K
# Testcase Example:  '[[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
# 
# Count the number of distinct islands.  An island is considered to be the same
# as another if they have the same shape, or have the same shape after rotation
# (90, 180, or 270 degrees only) or reflection (left/right direction or up/down
# direction).
# 
# Example 1:
# 
# 11000
# 10000
# 00001
# 00011
# 
# Given the above grid map, return 1.
# 
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
# are considered same island shapes. Because if we make a 180 degrees clockwise
# rotation on the first island, then two islands will have the same shapes.
# 
# 
# Example 2:
# 
# 11100
# 10001
# 01001
# 01110
# Given the above grid map, return 2.
# 
# Here are the two distinct islands:
# 
# 111
# 1
# 
# and
# 
# 1
# 1
# 
# 
# Notice that:
# 
# 111
# 1
# 
# and
# 
# 1
# 111
# 
# are considered same island shapes. Because if we flip the first array in the
# up/down direction, then they have the same shapes.
# 
# 
# Note:
# The length of each dimension in the given grid does not exceed 50.
# 
#
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        seen = set()
        def explore(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] and (r, c) not in seen:
                seen.add((r, c))
                shape.add(complex(r, c))
                explore(r+1, c)
                explore(r-1, c)
                explore(r, c+1)
                explore(r, c-1)

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape), min(z.imag for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = None
            for k in range(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans, translate([complex(z.imag, z.real) * (1j)**k for z in shape]))

            return tuple(ans)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c)
                if shape:
                    shapes.add(canonical(shape))

        return len(shapes)
        

