#
# @lc app=leetcode id=2132 lang=python3
#
# [2132] Stamping the Grid
#

# @lc code=start
import itertools

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:

        def acc_2d(grid):
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for r, c in itertools.product(range(m), range(n)):
                dp[r + 1][c + 1] = dp[r + 1][c] + dp[r][c + 1] - dp[r][c] + grid[r][c]
            return dp

        def sumRegion(r1, c1, r2, c2):
            return dp[r2 + 1][c2 + 1] - dp[r1][c2 + 1] - dp[r2 + 1][c1] + dp[r1][c1]

        m, n = map(len, (grid, grid[0]))
        dp = acc_2d(grid)

        diff = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - stampHeight + 1):
            for c in range(n - stampWidth + 1):
                if sumRegion(r, c, r + stampHeight - 1, c + stampWidth - 1) == 0:
                    diff[r][c] += 1
                    diff[r + stampHeight][c] -= 1
                    diff[r][c + stampWidth] -= 1
                    diff[r + stampHeight][c + stampWidth] += 1

        dp2 = acc_2d(diff)
        for r, c in itertools.product(range(m), range(n)):
            if dp2[r + 1][c + 1] == 0 and grid[r][c] != 1:
                return False

        return True
                    

        
# @lc code=end

