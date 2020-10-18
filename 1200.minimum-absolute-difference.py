#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#
# https://leetcode.com/problems/minimum-absolute-difference/description/
#
# algorithms
# Easy (66.22%)
# Likes:    133
# Dislikes: 12
# Total Accepted:    23.4K
# Total Submissions: 35.4K
# Testcase Example:  '[4,2,1,3]'
#
# Given an array of distinct integers arr, find all pairs of elements with the
# minimum absolute difference of any two elements. 
# 
# Return a list of pairs in ascending order(with respect to pairs), each pair
# [a, b] follows
# 
# 
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in
# arr
# 
# 
# 
# Example 1:
# 
# 
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with
# difference equal to 1 in ascending order.
# 
# Example 2:
# 
# 
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# 
# 
# Example 3:
# 
# 
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]
        
# @lc code=end

