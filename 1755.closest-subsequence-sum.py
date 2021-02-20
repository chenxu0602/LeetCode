#
# @lc app=leetcode id=1755 lang=python3
#
# [1755] Closest Subsequence Sum
#
# https://leetcode.com/problems/closest-subsequence-sum/description/
#
# algorithms
# Hard (35.81%)
# Likes:    149
# Dislikes: 37
# Total Accepted:    3.8K
# Total Submissions: 10.6K
# Testcase Example:  '[5,-7,3,5]\n6'
#
# You are given an integer array nums and an integer goal.
# 
# You want to choose a subsequence of nums such that the sum of its elements is
# the closest possible to goal. That is, if the sum of the subsequence's
# elements is sum, then you want to minimize the absolute difference abs(sum -
# goal).
# 
# Return the minimum possible value of abs(sum - goal).
# 
# Note that a subsequence of an array is an array formed by removing some
# elements (possibly all or none) of the original array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,-7,3,5], goal = 6
# Output: 0
# Explanation: Choose the whole array as a subsequence, with a sum of 6.
# This is equal to the goal, so the absolute difference is 0.
# 
# 
# Example 2:
# 
# 
# Input: nums = [7,-9,15,-2], goal = -5
# Output: 1
# Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
# The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the
# minimum.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3], goal = -7
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 40
# -10^7 <= nums[i] <= 10^7
# -10^9 <= goal <= 10^9
# 
# 
#

# @lc code=start
import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def fn(nums):
            ans = {0}
            for x in nums:
                ans |= {x + y for y in ans}
            return ans

        nums2 = sorted(fn(nums[:len(nums) // 2]))

        ans = float("inf")
        for x in fn(nums[len(nums) // 2:]):
            i = bisect.bisect_left(nums2, goal - x)
            if i < len(nums2):
                ans = min(ans, nums2[i] + x - goal)
            if i > 0:
                ans = min(ans, goal - x - nums2[i - 1])

        return ans
        
# @lc code=end

