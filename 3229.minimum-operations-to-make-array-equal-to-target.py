#
# @lc app=leetcode id=3229 lang=python3
#
# [3229] Minimum Operations to Make Array Equal to Target
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:

        res = abs(nums[0] - target[0])

        for i in range(1, len(nums)):
            pre, cur = nums[i - 1] - target[i - 1], nums[i] - target[i]
            if (pre > 0 and cur > 0) or (pre < 0 and cur < 0):
                res += max(0, abs(cur) - abs(pre))
            else:
                res += abs(cur)

        return res
        
# @lc code=end

