#
# @lc app=leetcode id=2560 lang=python3
#
# [2560] House Robber IV
#

# @lc code=start
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            last = take = 0
            for a in nums:
                if last:
                    last = 0
                    continue
                if a <= mid:
                    take += 1
                    last = 1

            if take >= k:
                right = mid
            else:
                left = mid + 1

        return left
        
# @lc code=end

