#
# @lc app=leetcode id=3299 lang=python3
#
# [3299] Sum of Consecutive Subsequences
#

# @lc code=start
from collections import defaultdict, Counter

class Solution:
    def getSum(self, nums: List[int]) -> int:

        MOD = 10**9 + 7

        def dp(dir, res=0):
            count, sum_ = defaultdict(int), defaultdict(int)

            for num in nums:
                count[num] += count[num + dir] + 1
                sum_[num]  += sum_[num + dir] + num * (count[num + dir] + 1)
                res        += sum_[num + dir] + num * count[num + dir]

            return res % MOD

        return (sum(nums) + dp(-1) + dp(1)) % MOD

        
# @lc code=end

