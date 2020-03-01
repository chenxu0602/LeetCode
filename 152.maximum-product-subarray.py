#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.79%)
# Likes:    2622
# Dislikes: 115
# Total Accepted:    251K
# Total Submissions: 830.4K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # imin = imax = r = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] < 0:
        #         imin, imax = imax, imin
            
        #     imin = min(nums[i], imin*nums[i])
        #     imax = max(nums[i], imax*nums[i])

        #     r = max(r, imax)
        # return r


        A = nums[:]
        B = nums[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(A + B)

        
# @lc code=end

