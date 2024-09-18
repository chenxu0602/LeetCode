#
# @lc app=leetcode id=3250 lang=python3
#
# [3250] Find the Count of Monotonic Pairs I
#

# @lc code=start
from math import comb

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:

        """
        # Time  complexity: O(nx51x51)
        # Space complexity: O(nx51)

        MOD = 10**9 + 7
        n = len(nums)

        dp = [[0] * 51 for _ in range(n)]
        for j in range(nums[0] + 1):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(nums[i] + 1):
                for p in range(j + 1):
                    arr2_j = nums[i] - j
                    arr2_p = nums[i - 1] - p
                    if arr2_j <= arr2_p:
                        dp[i][j] += dp[i - 1][p]

        return sum(dp[-1]) % MOD
        """

        MOD = 10**9 + 7
        n = len(nums)
        max_ = nums.pop(0)

        n1, n2 = 0, max_
        for num in nums:
            if num < n1: return 0
            if num > n1 + n2:
                n1 = num - n2

            n2 = num - n1

            if n2 < max_:
                max_ = n2

        return  comb(n + max_, max_) % MOD

        
# @lc code=end

