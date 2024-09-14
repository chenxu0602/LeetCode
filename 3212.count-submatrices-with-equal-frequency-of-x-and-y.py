#
# @lc app=leetcode id=3212 lang=python3
#
# [3212] Count Submatrices With Equal Frequency of X and Y
#

# @lc code=start
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:

        m, n = map(len, (grid, grid[0]))
        x_col_sum, y_col_sum = [0] * n, [0] * n
        cnt = 0

        for i in range(m):
            cur_x = cur_y = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    x_col_sum[j] += 1
                if grid[i][j] == 'Y':
                    y_col_sum[j] += 1

                cur_x += x_col_sum[j]
                cur_y += y_col_sum[j]

                if cur_x == cur_y and cur_x > 0:
                    cnt += 1

        return cnt
        
# @lc code=end

