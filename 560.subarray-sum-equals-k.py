#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (42.43%)
# Likes:    2201
# Dislikes: 60
# Total Accepted:    119.4K
# Total Submissions: 280.7K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count, p, d = 0, 0, {0: 1}
        for i in nums:
            p += i
            if p - k in d:
                count += d[p-k]
            d[p] = d.get(p, 0) + 1
        return count
        

