#
# @lc app=leetcode id=2312 lang=python3
#
# [2312] Selling Pieces of Wood
#

# @lc code=start
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for r, c, p in prices:
            dp[r][c] = p

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                for nc in range(1, c // 2 + 1):
                    dp[r][c] = max(dp[r][c], dp[r][nc] + dp[r][c - nc])
                for nr in range(1, r // 2 + 1):
                    dp[r][c] = max(dp[r][c], dp[nr][c] + dp[r - nr][c])

        return dp[m][n]

        
# @lc code=end

