#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/description/
#
# algorithms
# Medium (46.42%)
# Likes:    117
# Dislikes: 15
# Total Accepted:    4.8K
# Total Submissions: 10.3K
# Testcase Example:  '[4,9,3]\n10'
#
# Given an integer array arr and a target value target, return the integer
# value such that when we change all the integers larger than value in the
# given array to be equal to value, the sum of the array gets as close as
# possible (in absolute difference) to target.
# 
# In case of a tie, return the minimum such integer.
# 
# Notice that the answer is not neccesarilly a number from arr.
# 
# 
# Example 1:
# 
# 
# Input: arr = [4,9,3], target = 10
# Output: 3
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's
# the optimal answer.
# 
# 
# Example 2:
# 
# 
# Input: arr = [2,3,5], target = 10
# Output: 5
# 
# 
# Example 3:
# 
# 
# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 1 <= arr[i], target <= 10^5
# 
#

# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse=True)
        maxA = arr[0]
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
        return int((target + len(arr) / 2.0 - 0.1) / len(arr)) if arr else maxA
        
# @lc code=end

