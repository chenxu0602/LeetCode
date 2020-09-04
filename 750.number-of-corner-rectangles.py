#
# @lc app=leetcode id=750 lang=python3
#
# [750] Number Of Corner Rectangles
#
# https://leetcode.com/problems/number-of-corner-rectangles/description/
#
# algorithms
# Medium (66.16%)
# Likes:    378
# Dislikes: 53
# Total Accepted:    24.1K
# Total Submissions: 36.3K
# Testcase Example:  '[[0,1,0],[1,0,1],[1,0,1],[0,1,0]]'
#
# Given a grid where each entry is only 0 or 1, find the number of corner
# rectangles.
# 
# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned
# rectangle. Note that only the corners need to have the value 1. Also, all
# four 1s used must be distinct.
# 
# 
# 
# Example 1:
# 
# 
# Input: grid = 
# [[1, 0, 0, 1, 0],
# ⁠[0, 0, 1, 0, 1],
# ⁠[0, 0, 0, 1, 0],
# ⁠[1, 0, 1, 0, 1]]
# Output: 1
# Explanation: There is only one corner rectangle, with corners grid[1][2],
# grid[1][4], grid[3][2], grid[3][4].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: grid = 
# [[1, 1, 1],
# ⁠[1, 1, 1],
# ⁠[1, 1, 1]]
# Output: 9
# Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and
# one 3x3 rectangle.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: grid = 
# [[1, 1, 1, 1]]
# Output: 0
# Explanation: Rectangles must have four distinct corners.
# 
# 
# 
# 
# Note:
# 
# 
# The number of rows and columns of grid will each be in the range [1,
# 200].
# Each grid[i][j] will be either 0 or 1.
# The number of 1s in the grid will be at most 6000.
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter
import itertools

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        # Time  complexity: O(R x C^2)
        # Space complexity: O(C^2)
        # count = Counter()
        # ans = 0
        # for row in grid:
        #     for c1, v1 in enumerate(row):
        #         if v1:
        #             for c2 in range(c1 + 1, len(row)):
        #                 if row[c2]:
        #                     ans += count[c1, c2]
        #                     count[c1, c2] += 1

        # return ans


        # Time  complexity: O(N x sqrt(N) + R x C) where N is the number of ones in the grid.
        # Space complexity: O(N + R + C^2)
        rows = [[c for c, val in enumerate(row) if val] for row in grid]
        N = sum(len(row) for row in grid)
        SQRTN = int(N**.5)

        ans = 0
        count = Counter()
        for r, row in enumerate(rows):
            if len(row) >= SQRTN:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= SQRTN:
                        continue
                    found = sum(1 for c2 in row2 if c2 in target)
                    ans += found * (found - 1) // 2
            else:
                for pair in itertools.combinations(row, 2):
                    ans += count[pair]
                    count[pair] += 1

        return ans

        
# @lc code=end

