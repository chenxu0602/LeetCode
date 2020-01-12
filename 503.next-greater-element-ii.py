#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (51.48%)
# Likes:    730
# Dislikes: 44
# Total Accepted:    53.7K
# Total Submissions: 104.3K
# Testcase Example:  '[1,2,1]'
#
# 
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
# 
# 
# Example 1:
# 
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
# 
# 
# 
# Note:
# The length of given array won't exceed 10000.
# 
#
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        n = len(nums)
        ans = [-1] * n
        stack, i = [], n - 1
        for _ in range(2 * n):
            cur = nums[i]
            while stack and stack[-1] <= cur:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(cur)
            i -= 1
            if i == -1:
                i = n - 1
        return ans
        """

        stack, res = [], [-1] * len(nums)
        for i in list(range(len(nums))) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
        

