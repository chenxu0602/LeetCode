#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (42.21%)
# Likes:    1886
# Dislikes: 54
# Total Accepted:    134.7K
# Total Submissions: 319.2K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# Note:
# 
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# 
#

# @lc code=start
from functools import lru_cache 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        possible = {0}
        for n in nums:
            possible.update({v + n for v in possible})
        return sum(nums) / 2. in possible

        # target, n = sum(nums), len(nums)
        # if target & 1: return False
        # target >>= 1
        # dp = [True] + [False] * target
        # for n in nums:
        #     dp = [dp[s] or (s >= n and dp[s-n]) for s in range(target+1)]
        # return dp[target]
        
        
# @lc code=end

