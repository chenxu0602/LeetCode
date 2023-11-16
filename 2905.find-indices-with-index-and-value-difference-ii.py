#
# @lc app=leetcode id=2905 lang=python3
#
# [2905] Find Indices With Index and Value Difference II
#

# @lc code=start
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        min_i = max_i = 0
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[min_i]: min_i = i - indexDifference
            if nums[i - indexDifference] > nums[max_i]: max_i = i - indexDifference

            if nums[i] - nums[min_i] >= valueDifference:
                return [min_i, i]

            if nums[max_i] - nums[i] >= valueDifference:
                return [max_i, i]

        return [-1, -1]
        
# @lc code=end

