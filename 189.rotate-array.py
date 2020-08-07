#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (34.54%)
# Likes:    2951
# Dislikes: 823
# Total Accepted:    508.5K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Follow up:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# It's guaranteed that nums[i] fits in a 32 bit-signed integer.
# k >= 0
# 
# 
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Using Cyclic Replacements
        # Time  complexity: O(n)
        # Space complexity: O(1)
        # n = len(nums)
        # k %= n

        # start = count = 0
        # while count < n:
        #     current, prev = start, nums[start]
        #     while True:
        #         next_idx = (current + k) % n
        #         nums[next_idx], prev = prev, nums[next_idx]
        #         current = next_idx
        #         count += 1

        #         if start == current:
        #             break
        #     start += 1


        # Using Reverse
        # Time  complexity: O(n)
        # Space complexity: O(1)
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        n = len(nums)
        k %= n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

        
# @lc code=end

