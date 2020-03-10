#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort
#
# https://leetcode.com/problems/wiggle-sort/description/
#
# algorithms
# Medium (61.50%)
# Likes:    472
# Dislikes: 49
# Total Accepted:    73.2K
# Total Submissions: 118.2K
# Testcase Example:  '[3,5,2,1,6,4]'
#
# Given an unsorted array nums, reorder it in-place such that nums[0] <=
# nums[1] >= nums[2] <= nums[3]....
# 
# Example:
# 
# 
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]
# 
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-1):
            if (i % 2 == 0) == (nums[i] > nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]

        
# @lc code=end

