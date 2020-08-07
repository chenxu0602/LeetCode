#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (58.38%)
# Likes:    3521
# Dislikes: 304
# Total Accepted:    380.2K
# Total Submissions: 651K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [0] * n
        answer[0] = 1

        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        R = 1
        for i in range(n-1, -1, -1):
            answer[i] *= R
            R *= nums[i]

        return answer
        
# @lc code=end

