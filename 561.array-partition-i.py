#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#
# https://leetcode.com/problems/array-partition-i/description/
#
# algorithms
# Easy (69.49%)
# Likes:    593
# Dislikes: 1800
# Total Accepted:    154.6K
# Total Submissions: 222.2K
# Testcase Example:  '[1,4,3,2]'
#
# 
# Given an array of 2n integers, your task is to group these integers into n
# pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of
# min(ai, bi) for all i from 1 to n as large as possible.
# 
# 
# Example 1:
# 
# Input: [1,4,3,2]
# 
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3,
# 4).
# 
# 
# 
# Note:
# 
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
# 
# 
#
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        nums.sort()
        s = 0
        for i in range(0, len(nums), 2):
            s += nums[i]

        return s
        """

        arr = [0] * 20001
        lim = 10000

        for num in nums:
            arr[num+lim] += 1

        d, sums = 0, 0
        for i in range(-10000, 10001):
            sums += (arr[i+lim]+1-d) // 2 * i
            d = (2 + arr[i+lim]-d) % 2
        
        return sums

