#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (32.47%)
# Likes:    1536
# Dislikes: 290
# Total Accepted:    298.1K
# Total Submissions: 915.8K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def twoSum(nums, target):
            res, s = [], set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])                    
            return res

        def kSum(nums, target , k):
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []

            if k == 2:
                return twoSum(nums, target)

            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i+1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)

            return res

        # Time complexity is O(n^(k-1))
        nums.sort()
        return kSum(nums, target, 4)
        
# @lc code=end

