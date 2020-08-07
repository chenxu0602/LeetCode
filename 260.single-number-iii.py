#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (59.44%)
# Likes:    1162
# Dislikes: 90
# Total Accepted:    125.3K
# Total Submissions: 210.8K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# Example:
# 
# 
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# 
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        # x & (-x) is a way to isolate the rightmost 1-bit
        # x & (-x) keeps the rightmost 1-bit and sets all the other bits to 0

        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num

        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num

        return [x, bitmask^x]
        
# @lc code=end

