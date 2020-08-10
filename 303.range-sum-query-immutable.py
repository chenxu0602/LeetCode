#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (44.42%)
# Likes:    923
# Dislikes: 1096
# Total Accepted:    206.7K
# Total Submissions: 462.7K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' + '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# Example:
# 
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Constraints:
# 
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 0 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= i <= j < nums.length
# 
# 
#

# @lc code=start
import itertools

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] + list(itertools.accumulate(nums))
        
    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j + 1] - self.nums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

