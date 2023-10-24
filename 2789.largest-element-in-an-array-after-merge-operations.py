#
# @lc app=leetcode id=2789 lang=python3
#
# [2789] Largest Element in an Array after Merge Operations
#

# @lc code=start
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:

        # n = len(nums)
        # for i in range(n - 1, 0, -1):
        #     if nums[i - 1] <= nums[i]:
        #         nums[i - 1] += nums[i]

        # return nums[0]


        stack = []
        for num in reversed(nums):
            while stack and num <= stack[-1]:
                num += stack.pop()
            stack += num, 

        return stack[-1]
        
# @lc code=end

