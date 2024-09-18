#
# @lc app=leetcode id=3240 lang=python3
#
# [3240] Minimum Number of Flips to Make Binary Grid Palindromic II
#

# @lc code=start
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:

        m, n = map(len, (grid, grid[0]))
        res, single, double = 0, 0, 0

        for i in range(m // 2):
            for j in range(n // 2):
                ones = grid[i][j] + grid[i][~j] + grid[~i][j] + grid[~i][~j]
                res += min(ones, 4 - ones)

            if n % 2 == 1:
                ones = grid[i][n // 2] + grid[~i][n // 2]
                single += (ones == 1)
                double += (ones == 2)

        if m % 2 == 1:
            for j in range(n // 2):
                ones = grid[m // 2][j] + grid[m // 2][~j]
                single += (ones == 1)
                double += (ones == 2)

            if n % 2 == 1:
                res += grid[m // 2][n // 2]

        
        if double % 2 == 0 or single > 0:
            return res + single

        return res + 2
        
# @lc code=end

