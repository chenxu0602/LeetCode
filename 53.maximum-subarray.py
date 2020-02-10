#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.25%)
# Likes:    5284
# Dislikes: 213
# Total Accepted:    657.7K
# Total Submissions: 1.5M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for i in nums[1:]:
            curSum = max(i, curSum + i)
            maxSum = max(maxSum, curSum)

        return maxSum
        """

        curSum = 0
        maxSum = float("-inf")
        
        for i in nums:
            curSum += i
            maxSum = max(maxSum, curSum)
            curSum = max(0, curSum)
        return maxSum
        
# @lc code=end

