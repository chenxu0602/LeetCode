#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (53.67%)
# Likes:    2050
# Dislikes: 179
# Total Accepted:    449.5K
# Total Submissions: 824.6K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#

# @lc code=start
from random import choice 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        """
        majority_count = len(nums) // 2
        while True:
            candidate = choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
        """

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
        
# @lc code=end

