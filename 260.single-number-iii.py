#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (57.07%)
# Likes:    845
# Dislikes: 76
# Total Accepted:    107.3K
# Total Submissions: 188K
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
from functools import reduce 

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        xor = reduce(lambda x, y: x ^ y, nums, 0)

        mask = 1
        while not xor & 1:
            xor >>= 1
            mask <<= 1

        zero = one = 0
        for num in nums:
            if num & mask:
                one ^= num
            else:
                zero ^= num

        if zero > one:
            zero, one = one, zero

        return zero, one
        """

        bitmask = 0
        for num in nums:
            bitmask ^= num

        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]

        

