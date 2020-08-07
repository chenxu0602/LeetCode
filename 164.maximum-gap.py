#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap/description/
#
# algorithms
# Hard (35.33%)
# Likes:    859
# Dislikes: 182
# Total Accepted:    89.2K
# Total Submissions: 252K
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
    def countingSort(self, arr, exp1):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            idx = arr[i] // exp1
            count[idx % 10] += 1

        for i in range(1, 10):
            count[i] += count[i-1]

        i = n - 1
        while i >= 0:
            idx = arr[i] // exp1
            output[count[idx % 10] - 1] = arr[i]
            count[idx % 10] -= 1
            i -= 1

        for i in range(len(arr)):
            arr[i] = output[i]

    def maximumGap(self, nums: List[int]) -> int:
        # Radix Sort
        # Time  complexity: O(d(n + k))
        # Space complexity: O(n)
        # if not nums:
        #     return 0

        # max1 = max(nums)
        # exp = 1
        # while max1 // exp > 0:
        #     self.countingSort(nums, exp)
        #     exp *= 10

        # maxGap = 0        
        # for i in range(len(nums) - 1):
        #     maxGap = max(nums[i+1] - nums[i], maxGap)

        # return maxGap


        # Buckets and The Pigeonhole Principle
        # Time  complexity: O(n + b)
        # Space complexity: O(b)
        if len(nums) < 2 or max(nums) == min(nums):
            return 0

        a, b = min(nums), max(nums)

        size = (b - a) // (len(nums) - 1) or 1

        bucket = [[None, None] for _ in range((b - a) // size + 1)]

        for n in nums:
            b = bucket[(n - a) // size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0] - bucket[i-1][1] for i in range(1, len(bucket)))

        
# @lc code=end

