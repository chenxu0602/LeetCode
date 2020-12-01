#
# @lc app=leetcode id=1567 lang=python3
#
# [1567] Maximum Length of Subarray With Positive Product
#
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/description/
#
# algorithms
# Medium (36.08%)
# Likes:    316
# Dislikes: 4
# Total Accepted:    11.1K
# Total Submissions: 30.6K
# Testcase Example:  '[1,-2,-3,4]'
#
# Given an array of integers nums, find the maximum length of a subarray where
# the product of all its elements is positive.
# 
# A subarray of an array is a consecutive sequence of zero or more values taken
# out of that array.
# 
# Return the maximum length of a subarray with positive product.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which
# has a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the
# product 0 which is not positive.
# 
# Example 3:
# 
# 
# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or
# [-2,-3].
# 
# 
# Example 4:
# 
# 
# Input: nums = [-1,2]
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: nums = [1,2,3,5,-6,4,0,10]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for x in nums:
            if x > 0:
                pos, neg = 1 + pos, 1 + neg if neg else 0
            elif x < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos = neg = 0

            ans = max(ans, pos)

        return ans
        
# @lc code=end

