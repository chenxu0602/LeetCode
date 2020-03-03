#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
#
# algorithms
# Hard (44.91%)
# Likes:    744
# Dislikes: 39
# Total Accepted:    33K
# Total Submissions: 73.4K
# Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
#
# In a given array nums of positive integers, find three non-overlapping
# subarrays with maximum sum.
# 
# Each subarray will be of size k, and we want to maximize the sum of all 3*k
# entries.
# 
# Return the result as a list of indices representing the starting position of
# each interval (0-indexed). If there are multiple answers, return the
# lexicographically smallest one.
# 
# Example:
# 
# 
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting
# indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be
# lexicographically larger.
# 
# 
# 
# 
# Note:
# 
# 
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], K: int) -> List[int]:
        W = []
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K - 1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W)-1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(K, len(W)-K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k

        return ans
        
# @lc code=end

