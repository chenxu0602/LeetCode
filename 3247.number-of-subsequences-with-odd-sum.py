#
# @lc app=leetcode id=3247 lang=python3
#
# [3247] Number of Subsequences with Odd Sum
#

# @lc code=start
class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:

        """
        MOD = 10**9 + 7

        odd = even = 0
        for num in nums:
            if not num % 2:
                odd, even = odd * 2, even * 2 + 1
            else:
                odd, even = odd + even + 1, even + odd

        return odd % MOD
        """

        MOD = 10**9 + 7
        n = len(nums)
        return pow(2, n - 1, MOD) if any(num % 2 for num in nums) else 0
        
# @lc code=end

