#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (58.56%)
# Likes:    3348
# Dislikes: 224
# Total Accepted:    668.3K
# Total Submissions: 1.1M
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
import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Randomization
        # Time  complexity: worst case O(Infinity), average linear
        # Space complexity: O(1)
        # majority_count = len(nums) // 2
        # while True:
        #     candidate = random.choice(nums)
        #     if sum(1 for elem in nums if elem == candidate) > majority_count:
        #         return candidate


        # Boyer-Moore Voting Algorithm
        # Time  complexity: O(n)
        # Space complexity: O(1)
        count, candidate = 0, None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

        
# @lc code=end

