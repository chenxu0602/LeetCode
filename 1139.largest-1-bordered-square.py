#
# @lc app=leetcode id=1139 lang=python3
#
# [1139] Largest 1-Bordered Square
#
# https://leetcode.com/problems/largest-1-bordered-square/description/
#
# algorithms
# Medium (47.34%)
# Likes:    242
# Dislikes: 54
# Total Accepted:    11.2K
# Total Submissions: 23.4K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D grid of 0s and 1s, return the number of elements in the largest
# square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't
# exist in the grid.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 9
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,1,0,0]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] is 0 or 1
# 
#

# @lc code=start
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = map(len, (grid, grid[0]))
        biggest, dp = 0, [[(0, 0) for _ in range(n + 1)] for _ in range(m + 1)]

        for r in range(m)[::-1]:
            for c in range(n)[::-1]:
                if grid[r][c]:
                    dp[r][c] = (1 + dp[r+1][c][0], 1 + dp[r][c+1][1])
                    if min(dp[r][c]) > biggest:
                        for side in range(biggest, 1 + min(dp[r][c]))[::-1]:
                            if side <= dp[r + side - 1][c][1] and side <= dp[r][c + side - 1][0]:
                                biggest = side
                                break

        return biggest ** 2


        
# @lc code=end

