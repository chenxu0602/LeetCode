#
# @lc app=leetcode id=1224 lang=python3
#
# [1224] Maximum Equal Frequency
#
# https://leetcode.com/problems/maximum-equal-frequency/description/
#
# algorithms
# Hard (32.74%)
# Likes:    125
# Dislikes: 16
# Total Accepted:    4.6K
# Total Submissions: 13.9K
# Testcase Example:  '[2,2,1,1,5,3,3,5]'
#
# Given an array nums of positive integers, return the longest possible length
# of an array prefix of nums, such that it is possible to remove exactly one
# element from this prefix so that every number that has appeared in it will
# have the same number of occurrences.
# 
# If after removing one element there are no remaining elements, it's still
# considered that every appeared number has the same number of ocurrences
# (0).
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,2,1,1,5,3,3,5]
# Output: 7
# Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove
# nums[4]=5, we will get [2,2,1,1,3,3], so that each number will appear exactly
# twice.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# Output: 13
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,1,2,2,2]
# Output: 5
# 
# 
# Example 4:
# 
# 
# Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
# Output: 8
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = Counter()
        freq = [0] * (len(nums) + 1)

        res = 0

        for n, a in enumerate(nums, 1):
            freq[count[a]] -= 1
            freq[count[a] + 1] += 1

            c = count[a] = count[a] + 1

            if freq[c] * c == n and n < len(nums):
                res = n + 1

            d = n - freq[c] * c
            if d in [c + 1, 1] and freq[d] == 1:
                res = n

        return res


# @lc code=end

