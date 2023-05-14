#
# @lc app=leetcode id=2681 lang=python3
#
# [2681] Power of Heroes
#

# @lc code=start
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:

        ans, t, MOD = 0, 0, 10**9 + 7
        for n in sorted(nums):
            ans = (ans + (t + n) * n * n) % MOD
            t = (2 * t + n) % MOD
        return ans
        
# @lc code=end

