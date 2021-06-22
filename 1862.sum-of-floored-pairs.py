#
# @lc app=leetcode id=1862 lang=python3
#
# [1862] Sum of Floored Pairs
#
# https://leetcode.com/problems/sum-of-floored-pairs/description/
#
# algorithms
# Hard (27.19%)
# Likes:    188
# Dislikes: 19
# Total Accepted:    4.1K
# Total Submissions: 15K
# Testcase Example:  '[2,5,9]'
#
# Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for
# all pairs of indices 0 <= i, j < nums.length in the array. Since the answer
# may be too large, return it modulo 10^9 + 7.
# 
# The floor() function returns the integer part of the division.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,5,9]
# Output: 10
# Explanation:
# floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
# floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
# floor(5 / 2) = 2
# floor(9 / 2) = 4
# floor(9 / 5) = 1
# We calculate the floor of the division for every pair of indices in the array
# then sum them up.
# 
# 
# Example 2:
# 
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 49
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
from collections import Counter
import itertools

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:

        incs, counter = [0] * (max(nums) + 1), Counter(nums)
        for num in counter:
            for j in range(num, len(incs), num):
                incs[j] += counter[num]

        quots = list(itertools.accumulate(incs))
        return sum(quots[num] for num in nums) % (10**9 + 7)

        
# @lc code=end

