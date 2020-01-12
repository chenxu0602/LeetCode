#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (20.00%)
# Likes:    791
# Dislikes: 795
# Total Accepted:    103.4K
# Total Submissions: 511.7K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1

        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m-1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m+1]) < w:
                return True
            d[m] = nums[i]

            if i >= k:
                del d[nums[i-k]//w]
        return False
        
# @lc code=end

