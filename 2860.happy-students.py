#
# @lc app=leetcode id=2860 lang=python3
#
# [2860] Happy Students
#

# @lc code=start
class Solution:
    def countWays(self, nums: List[int]) -> int:

        # nums = [float("-inf")] + sorted(nums) + [float("inf")]
        # cnt = 0
        # for i in range(1, len(nums)):
        #     if nums[i - 1] < i - 1 < nums[i]:
        #         cnt += 1

        # return cnt


        # nums.sort()
        # cnt = 0
        # for i in range(1, len(nums) - 1):
        #     if nums[i - 1] < i < nums[i]:
        #         cnt += 1

        # if min(nums) > 0: cnt += 1
        # if max(nums) < len(nums): cnt += 1

        # return cnt


        ans = 0
        nums.sort()
        if nums[0] > 0: ans += 1
        for i in range(len(nums)):
            if nums[i] < i + 1 and (i + 1 == len(nums) or i + 1 < nums[i + 1]):
                ans += 1

        return ans
        
# @lc code=end

