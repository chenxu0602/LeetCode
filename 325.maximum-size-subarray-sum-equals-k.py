#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
#
# algorithms
# Medium (46.11%)
# Likes:    769
# Dislikes: 28
# Total Accepted:    92.5K
# Total Submissions: 200.5K
# Testcase Example:  '[1,-1,5,-2,3]\n3'
#
# Given an array nums and a target value k, find the maximum length of a
# subarray that sums to k. If there isn't one, return 0 instead.
# 
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit
# signed integer range.
# 
# Example 1:
# 
# 
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4 
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2 
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# 
# Follow Up:
# Can you do it in O(n) time?
# 
#

# @lc code=start
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        record, sum_, r = {}, 0, 0

        for i, num in enumerate(nums):
            sum_ += num

            if sum_ == k:
                r = i + 1
            elif sum_ - k in record:
                r = max(i - record[sum_ - k], r)

            record.setdefault(sum_, i)

        return r
        
# @lc code=end

