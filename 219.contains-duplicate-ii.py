#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (37.62%)
# Likes:    882
# Dislikes: 1048
# Total Accepted:    275.3K
# Total Submissions: 730.2K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Time:  complexity: O(n)
        # Space: complexity: O(min(n, k))
        # dic = set()
        # for i in range(len(nums)):
        #     if nums[i] in dic:
        #         return True
        #     dic.add(nums[i])
        #     if len(dic) > k:
        #         dic.remove(nums[i-k])
        # return False


        # Time:  complexity: O(n)
        # Space: complexity: O(n)
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
        
# @lc code=end

