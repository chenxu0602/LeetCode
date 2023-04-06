#
# @lc app=leetcode id=2547 lang=python3
#
# [2547] Minimum Cost to Split an Array
#

# @lc code=start
from functools import lru_cache
from collections import defaultdict

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:

        n = len(nums)
        dp = [0] + [float("inf")] * n
        for i in range(n):
            C = [0] * n
            val = k
            for j in range(i, -1, -1):
                val += (C[nums[j]] >= 1) + (C[nums[j]] == 1)
                C[nums[j]] += 1
                dp[i + 1] = min(dp[i + 1], dp[j] + val)

        return dp[-1]

        """
        @lru_cache(None)
        def dp(left, n = len(nums)): 
            if left == n: return 0

            tmp, ans, d = k, float("inf"), defaultdict(int)

            for right, num in enumerate(nums[left:], start = left):
                d[num] += 1
                tmp += (d[num] > 1) + (d[num] == 2)
                ans = min(ans, tmp + dp(right + 1))

            return ans

        return dp(0)
        """
        
# @lc code=end

