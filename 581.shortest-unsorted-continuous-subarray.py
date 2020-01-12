#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (30.28%)
# Likes:    1548
# Dislikes: 72
# Total Accepted:    74.1K
# Total Submissions: 244.2K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.  
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# 
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# 
# Note:
# 
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means . 
# 
# 
#
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        """
        nums2 = nums[:]
        nums2.sort()

        start = end = 0
        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                start = i
                break

        for i in range(len(nums)-1, 0, -1):
            if nums[i] != nums2[i]:
                end = i
                break

        return end - start + 1 if end - start else 0
        """

        stack = []
        l, r = len(nums), 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)

        return r - l + 1 if r - l > 0 else 0
        



