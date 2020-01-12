#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#
# https://leetcode.com/problems/random-pick-index/description/
#
# algorithms
# Medium (50.06%)
# Likes:    269
# Dislikes: 469
# Total Accepted:    56.7K
# Total Submissions: 112.8K
# Testcase Example:  '["Solution","pick"]\n[[[1,2,3,3,3]],[3]]'
#
# Given an array of integers with possible duplicates, randomly output the
# index of a given target number. You can assume that the given target number
# must exist in the array.
# 
# Note:
# The array size can be very large. Solution that uses too much extra space
# will not pass the judge.
# 
# Example:
# 
# 
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should
# have equal probability of returning.
# solution.pick(3);
# 
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
# 
# 
#
import heapq
from random import randint, random

class Solution:

    def __init__(self, nums: List[int]):

        self.nums = nums
        

    def pick(self, target: int) -> int:

        """
        heap = []
        for i, v in enumerate(self.nums):
            if v == target:
                heapq.heappush(heap, (random(), i))
            
        r, idx = heapq.heappop(heap)

        return idx
        """

        total, res = 0, -1
        for i, v in enumerate(self.nums):
            if v == target:
                x = randint(0, total)
                if x == 0:
                    res = i
                total += 1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

