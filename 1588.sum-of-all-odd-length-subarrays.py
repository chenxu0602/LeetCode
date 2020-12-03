#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/
#
# algorithms
# Easy (81.23%)
# Likes:    322
# Dislikes: 45
# Total Accepted:    20.3K
# Total Submissions: 25K
# Testcase Example:  '[1,4,2,5,3]'
#
# Given an array of positive integers arr, calculate the sum of all possible
# odd-length subarrays.
# 
# A subarray is a contiguous subsequence of the array.
# 
# Return the sum of all odd-length subarrays of arr.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 =
# 58
# 
# Example 2:
# 
# 
# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum
# is 3.
# 
# Example 3:
# 
# 
# Input: arr = [10,11,12]
# Output: 66
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 1000
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # n, sum_odd = len(arr), 0
        # p_sum = [0] + list(itertools.accumulate(arr))

        # for i, p in enumerate(p_sum):
        #     for j in range(i + 1, n + 1, 2):
        #         sum_odd += p_sum[j] - p_sum[i]

        # return sum_odd


        res, n = 0, len(arr)
        for i, a in enumerate(arr):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res
        
# @lc code=end

