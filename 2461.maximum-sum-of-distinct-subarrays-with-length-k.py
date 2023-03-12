#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        res, cur, pos, dup = 0, 0, [-1] * 100001, -1

        for i in range(len(nums)):
            cur += nums[i]
            if i >= k:
                cur -= nums[i - k]

            dup = max(dup, pos[nums[i]])

            if i - dup >= k:
                res = max(res, cur)


            pos[nums[i]] = i

        return res
        
# @lc code=end

