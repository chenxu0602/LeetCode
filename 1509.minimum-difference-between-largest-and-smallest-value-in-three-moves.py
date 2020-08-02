#
# @lc app=leetcode id=1509 lang=python3
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/
#
# algorithms
# Medium (50.88%)
# Likes:    153
# Dislikes: 16
# Total Accepted:    6.1K
# Total Submissions: 12K
# Testcase Example:  '[5,3,2,4]'
#
# Given an array nums, you are allowed to choose one element of nums and change
# it by any value in one move.
# 
# Return the minimum difference between the largest and smallest value of nums
# after perfoming at most 3 moves.
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,3,2,4]
# Output: 0
# Explanation: Change the array [5,3,2,4] to [2,2,2,2].
# The difference between the maximum and minimum is 2-2 = 0.
# 
# Example 2:
# 
# 
# Input: nums = [1,5,0,10,14]
# Output: 1
# Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
# The difference between the maximum and minimum is 1-0 = 1.
# 
# 
# Example 3:
# 
# 
# Input: nums = [6,6,0,1,1,4,6]
# Output: 2
# 
# 
# Example 4:
# 
# 
# Input: nums = [1,5,6,14,15]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
#

# @lc code=start
import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # nums.sort()
        # return min(b - a for a, b in zip(nums[:4], nums[-4:]))

        return min(a - b for a, b in zip(heapq.nlargest(4, nums), heapq.nsmallest(4, nums)[::-1]))
        
# @lc code=end

