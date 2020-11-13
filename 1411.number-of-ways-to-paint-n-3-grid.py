#
# @lc app=leetcode id=1411 lang=python3
#
# [1411] Number of Ways to Paint N × 3 Grid
#
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/
#
# algorithms
# Hard (60.63%)
# Likes:    355
# Dislikes: 22
# Total Accepted:    12.3K
# Total Submissions: 20.3K
# Testcase Example:  '1'
#
# You have a grid of size n x 3 and you want to paint each cell of the grid
# with exactly one of the three colours: Red, Yellow or Green while making sure
# that no two adjacent cells have the same colour (i.e no two cells that share
# vertical or horizontal sides have the same colour).
# 
# You are given n the number of rows of the grid.
# 
# Return the number of ways you can paint this grid. As the answer may grow
# large, the answer must be computed modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown:
# 
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 54
# 
# 
# Example 3:
# 
# 
# Input: n = 3
# Output: 246
# 
# 
# Example 4:
# 
# 
# Input: n = 7
# Output: 106494
# 
# 
# Example 5:
# 
# 
# Input: n = 5000
# Output: 30228214
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# grid[i].length == 3
# 1 <= n <= 5000
# 
#

# @lc code=start
class Solution:
    def numOfWays(self, n: int) -> int:
        # O(N)
        # color3, color2 = 6, 6
        # MOD = 10**9 + 7

        # for i in range(1, n):
        #     color3, color2 = (2 * color3 + 2 * color2) % MOD, (2 * color3 + 3 * color2) % MOD

        # return (color3 + color2) % MOD

        # O(logN)
        import numpy as np
        n, MOD = n - 1, 10**9 + 7
        M = np.matrix([[3, 2], [2, 2]])
        res = [6, 6]
        while n:
            if n % 2:
                res = res * M % MOD
            M = M * M % MOD
            n //= 2
        return (np.sum(res)) % MOD
        
# @lc code=end

