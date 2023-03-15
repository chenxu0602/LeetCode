#
# @lc app=leetcode id=2482 lang=python3
#
# [2482] Difference Between Ones and Zeros in Row and Column
#

# @lc code=start
import itertools

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        m, n = map(len, (grid, grid[0]))
        def count(nums):
            return 2 * sum(nums) - len(nums)

        rows = list(map(count, grid))
        cols = list(map(count, zip(*grid)))

        for i, j in itertools.product(range(m), range(n)):
            grid[i][j] = rows[i] + cols[j]

        return grid
        
# @lc code=end

