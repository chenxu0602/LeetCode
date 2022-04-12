#
# @lc app=leetcode id=2209 lang=python3
#
# [2209] Minimum White Tiles After Covering With Carpets
#

# @lc code=start
from functools import lru_cache

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        # dp[i][k] means that, using k tiles to cover the first i tiles
        # the minimum number of white tiles still visible.
        # For each tile s[i], we heve two options,
        # one option is doing nothing, jump this tile, jump = dp[i - 1][k] + int(s[i - 1]),
        # the other option is covering this tile cover = dp[i - l][k - 1].
        # Then we take the minimum result of two options: dp[i][k] = min(jump, cover).
        # Finally after explore all combination of (i,k), we return dp[n][nc].
        # Time  complexity: O(NC) where N = floor.length and C = numCarpets.
        # Space complexity: O(NC)
        @lru_cache(None)
        def dp(i, k):
            if i <= 0: return 0
            return min(int(floor[i - 1]) + dp(i - 1, k), dp(i - carpetLen, k - 1) if k else 1000)

        return dp(len(floor), numCarpets)
        
# @lc code=end

