#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (61.08%)
# Likes:    2939
# Dislikes: 113
# Total Accepted:    548.3K
# Total Submissions: 888.1K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#

# @lc code=start

from functools import reduce 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return 2 * sum(set(nums)) - sum(nums)

        # a = 0
        # for i in nums:
        #     a ^= i
        # return a

        return reduce(lambda x, y: x ^ y, nums)
        
# @lc code=end

