#
# @lc app=leetcode id=2218 lang=python3
#
# [2218] Maximum Value of K Coins From Piles
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # dp[i,k] means picking k elements from pile[i] to pile[n-1].
        # Time  complexity: O(nm), where m = sum(piles[i].length) <= 2000.
        # Space complexity: O(nk)
        @lru_cache(None)
        def dp(i, k):
            if k == 0 or i == len(piles):
                return 0

            res, cur = dp(i + 1, k), 0
            for j in range(min(len(piles[i]), k)):
                cur += piles[i][j]
                res = max(res, cur + dp(i + 1, k - j - 1))
            return res

        return dp(0, k)

        
# @lc code=end

