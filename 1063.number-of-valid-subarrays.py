#
# @lc app=leetcode id=1063 lang=python3
#
# [1063] Number of Valid Subarrays
#
# https://leetcode.com/problems/number-of-valid-subarrays/description/
#
# algorithms
# Hard (73.12%)
# Likes:    40
# Dislikes: 5
# Total Accepted:    1.6K
# Total Submissions: 2.2K
# Testcase Example:  '[1,4,2,5,3]'
#
# Given an array A of integers, return the number of non-empty continuous
# subarrays that satisfy the following condition:
# 
# The leftmost element of the subarray is not larger than other elements in the
# subarray.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,4,2,5,3]
# Output: 11
# Explanation: There are 11 valid subarrays:
# [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1]
# Output: 3
# Explanation: The 3 valid subarrays are: [3],[2],[1].
# 
# 
# Example 3:
# 
# 
# Input: [2,2,2]
# Output: 6
# Explanation: There are 6 valid subarrays:
# [2],[2],[2],[2,2],[2,2],[2,2,2].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# 0 <= A[i] <= 100000
# 
#
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:

        res, stack = 0, []
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            stack.append(n)
            res += len(stack)
        return res

        

