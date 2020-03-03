#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (24.43%)
# Likes:    980
# Dislikes: 1362
# Total Accepted:    98.3K
# Total Submissions: 402.6K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to a multiple of k, that is, sums up to n*k where n is also an
# integer.
# 
# 
# 
# Example 1:
# 
# 
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
# 
# 
# Example 2:
# 
# 
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
# 
# 
# 
# 
# Note:
# 
# 
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
# 
# 
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        d = {}
        d[0] = -1
        sum_ = 0

        for i, v in enumerate(nums):
            sum_ += v

            if k != 0:
                sum_ %= k

            if sum_ in d:
                if i - d[sum_] > 1:
                    return True
            else:
                d[sum_] = i

        return False

            

        
# @lc code=end

