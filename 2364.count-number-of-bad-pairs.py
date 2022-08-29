#
# @lc app=leetcode id=2364 lang=python3
#
# [2364] Count Number of Bad Pairs
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        """
        n = len(nums)
        tot = n * (n - 1) // 2
        good = 0
        dp = {}

        for i, num in enumerate(nums):
            v = i - num
            good += dp.get(v, 0)
            dp[v] = dp.get(v, 0) + 1

        return tot - good
        """

        m, ans = defaultdict(int), 0
        for i in range(len(nums)):
            ans += i - m[nums[i] - i]
            m[nums[i] - i] += 1
        return ans
        
# @lc code=end

