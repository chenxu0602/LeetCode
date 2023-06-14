#
# @lc app=leetcode id=2731 lang=python3
#
# [2731] Movement of Robots
#

# @lc code=start
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:

        for i in range(len(s)):
            if s[i] == 'L':
                nums[i] -= d
            else:
                nums[i] += d

        ans = 0
        nums.sort()
        MOD = 10**9 + 7
        s = 0

        for i in range(len(nums)):
            ans += (nums[i] * i - s) # i to its left
            ans %= MOD
            s += nums[i]
            s %= MOD

        return ans % MOD

        
# @lc code=end

