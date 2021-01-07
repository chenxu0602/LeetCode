#
# @lc app=leetcode id=1708 lang=python3
#
# [1708] Largest Subarray Length K
#
# https://leetcode.com/problems/largest-subarray-length-k/description/
#
# algorithms
# Easy (65.57%)
# Likes:    15
# Dislikes: 30
# Total Accepted:    964
# Total Submissions: 1.5K
# Testcase Example:  '[1,4,5,2,3]\n3'
#
# An array A is larger than some array B if for the first index i where A[i] !=
# B[i], A[i] > B[i].
# 
# For example, consider 0-indexing:
# 
# 
# [1,3,2,4] > [1,2,2,4], since at index 1, 3 > 2.
# [1,4,4,4] < [2,1,1,1], since at index 0, 1 < 2.
# 
# 
# A subarray is a contiguous subsequence of the array.
# 
# Given an integer array nums of distinct integers, return the largest subarray
# of nums of length k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,4,5,2,3], k = 3
# Output: [5,2,3]
# Explanation: The subarrays of size 3 are: [1,4,5], [4,5,2], and [5,2,3].
# Of these, [5,2,3] is the largest.
# 
# Example 2:
# 
# 
# Input: nums = [1,4,5,2,3], k = 4
# Output: [4,5,2,3]
# Explanation: The subarrays of size 4 are: [1,4,5,2], and [4,5,2,3].
# Of these, [4,5,2,3] is the largest.
# 
# Example 3:
# 
# 
# Input: nums = [1,4,5,2,3], k = 1
# Output: [5]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# All the integers of nums are unique.
# 
# 
# 
# Follow up: What if the integers in nums are not distinct?
#

# @lc code=start
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        # Time  complexity: O(N)
        # Space complexity: O(K)
        # mmax = max(nums[:len(nums) - k + 1])
        # idx = nums.index(mmax)
        # return nums[idx:idx + k]


        n, i, j, d = len(nums), 0, 1, 0
        while j + k - 1 < n:
            if nums[i + d] == nums[j + d] and d < k:
                d += 1
                continue
            if nums[i + d] < nums[j + d]:
                i = max(i + d + 1, j)
                j = i + 1
            else:
                j = j + d + 1

            d = 0
        return nums[i:i + k]
        
# @lc code=end

