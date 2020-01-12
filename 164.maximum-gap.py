#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap/description/
#
# algorithms
# Hard (33.10%)
# Likes:    605
# Dislikes: 142
# Total Accepted:    76.7K
# Total Submissions: 228.4K
# Testcase Example:  '[3,6,9,1]'
#
# Given an unsorted array, find the maximum difference between the successive
# elements in its sorted form.
# 
# Return 0 if the array contains less than 2 elements.
# 
# Example 1:
# 
# 
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
# (3,6) or (6,9) has the maximum difference 3.
# 
# Example 2:
# 
# 
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
# 
# Note:
# 
# 
# You may assume all elements in the array are non-negative integers and fit in
# the 32-bit signed integer range.
# Try to solve it in linear time/space.
# 
# 
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum = max(nums)
        bucket = [[] for i in range(10)]
        exp = 1

        while max_sum // exp > 0:
            for num in nums:
                bucket[(num//exp) % 10].append(num)
            nums = []
            for each in bucket:
                nums.extend(each)
            bucket = [[] for i in range(10)]
            exp *= 10

        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i-1])
        return max_gap
        
# @lc code=end

