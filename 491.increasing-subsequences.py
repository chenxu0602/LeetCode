#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#
# https://leetcode.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (42.36%)
# Likes:    432
# Dislikes: 80
# Total Accepted:    33.6K
# Total Submissions: 79.2K
# Testcase Example:  '[4,6,7,7]'
#
# Given an integer array, your task is to find all the different possible
# increasing subsequences of the given array, and the length of an increasing
# subsequence should be at least 2.
# 
# 
# 
# Example:
# 
# 
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
# 
# 
# 
# 
# Note:
# 
# 
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be
# considered as a special case of increasing sequence.
# 
# 
#
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs = {()}
        for num in nums:
            subs |= {sub + (num,)
                    for sub in subs
                    if not sub or sub[-1] <= num}

        return [sub for sub in subs if len(sub) >= 2]
        

