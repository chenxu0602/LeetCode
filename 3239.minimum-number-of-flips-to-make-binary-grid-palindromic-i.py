#
# @lc app=leetcode id=3239 lang=python3
#
# [3239] Minimum Number of Flips to Make Binary Grid Palindromic I
#

# @lc code=start
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:

        m, n = map(len, (grid, grid[0]))
        row_ans, col_ans = 0, 0

        row_ans = sum(row[i] ^ row[~i] for i in range(n // 2) for row in grid)

        grid = zip(*grid)

        for row in grid:
            for i in range(m // 2):
                col_ans += row[i] ^ row[~i]

        return min(row_ans, col_ans)
        
# @lc code=end

