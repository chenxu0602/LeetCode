#
# @lc app=leetcode id=2221 lang=python3
#
# [2221] Find Triangular Sum of an Array
#

# @lc code=start
class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        for j in range(len(nums), 0, -1):
            for i in range(1, j):
                nums[i - 1] += nums[i]
                nums[i - 1] %= 10

        return nums[0]
        
# @lc code=end

