#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#
# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (46.23%)
# Likes:    724
# Dislikes: 276
# Total Accepted:    76.7K
# Total Submissions: 165.6K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array, find three numbers whose product is maximum and
# output the maximum product.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: 6
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# Output: 24
# 
# 
# 
# 
# Note:
# 
# 
# The length of the given array will be in range [3,10^4] and all elements are
# in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of
# 32-bit signed integer.
# 
# 
# 
# 
#
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Time  complexity: O(nlogn)
        # Space complexity: O(logn)
        # nums = sorted(nums)
        # a = nums[0] * nums[1] * nums[-1]
        # b = nums[-3]*nums[-2]*nums[-1]

        # return max(a, b)


        min1, min2 = float("inf"), float("inf")
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")

        for n in nums:
            if n <= min1:
                min2, min1 = min1, n
            elif n <= min2:
                min2 = n

            if n >= max1:
                max3, max2, max1 = max2, max1, n
            elif n >= max2:
                max3, max2 = max2, n
            elif n >= max3:
                max3 = n

        return max(min1 * min2 * max1, max1 * max2 * max3)

        

