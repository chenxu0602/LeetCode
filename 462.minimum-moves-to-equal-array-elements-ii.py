#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
#
# algorithms
# Medium (52.50%)
# Likes:    359
# Dislikes: 30
# Total Accepted:    35.9K
# Total Submissions: 68.3K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty integer array, find the minimum number of moves required to
# make all array elements equal, where a move is incrementing a selected
# element by 1 or decrementing a selected element by 1.
# 
# You may assume the array's length is at most 10,000.
# 
# Example:
# 
# Input:
# [1,2,3]
# 
# Output:
# 2
# 
# Explanation:
# Only two moves are needed (remember each move increments or decrements one
# element):
# 
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# 
# 
#
class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        """
        n = len(nums)
        nums.sort()
        median = nums[n//2] if n % 2 else (nums[n//2-1] + nums[n//2]) // 2
        nums = [n - median for n in nums]
        return sum(abs(x) for x in nums)
        """

        nums.sort()
        l, r, s = 0, len(nums)-1, 0

        while l < r:
            s += nums[r] - nums[l]
            l += 1
            r -= 1

        return s

