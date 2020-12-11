#
# @lc app=leetcode id=1673 lang=python3
#
# [1673] Find the Most Competitive Subsequence
#
# https://leetcode.com/problems/find-the-most-competitive-subsequence/description/
#
# algorithms
# Medium (36.10%)
# Likes:    270
# Dislikes: 12
# Total Accepted:    6.8K
# Total Submissions: 18.7K
# Testcase Example:  '[3,5,2,6]\n2'
#
# Given an integer array nums and a positive integer k, return the most
# competitive subsequence of nums of size k.
# 
# An array's subsequence is a resulting sequence obtained by erasing some
# (possibly zero) elements from the array.
# 
# We define that a subsequence a is more competitive than a subsequence b (of
# the same length) if in the first position where a and b differ, subsequence a
# has a number less than the corresponding number in b. For example, [1,3,4] is
# more competitive than [1,3,5] because the first position they differ is at
# the final number, and 4 is less than 5.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]
# Explanation: Among the set of every possible subsequence: {[3,5], [3,2],
# [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,4,3,3,5,4,9,6], k = 4
# Output: [2,3,3,4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # Using Double-Ended Queue
        # O(n)

        n, stack = len(nums), []
        additional = n - k
        
        for i in range(n):
            while len(stack) > 0 and stack[-1] > nums[i] and additional > 0:
                stack.pop()
                additional -= 1
            stack.append(nums[i])
            
        return stack[:k]

        
# @lc code=end

