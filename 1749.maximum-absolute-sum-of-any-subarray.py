#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#
# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
#
# algorithms
# Medium (50.76%)
# Likes:    178
# Dislikes: 4
# Total Accepted:    6.6K
# Total Submissions: 12.9K
# Testcase Example:  '[1,-3,2,3,-4]'
#
# You are given an integer array nums. The absolute sum of a subarray [numsl,
# numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 +
# numsr).
# 
# Return the maximum absolute sum of any (possibly empty) subarray of nums.
# 
# Note that abs(x) is defined as follows:
# 
# 
# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8)
# = 8.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
import itertools 

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(itertools.accumulate(nums, initial=0)) - min(itertools.accumulate(nums, initial=0))
        
# @lc code=end

