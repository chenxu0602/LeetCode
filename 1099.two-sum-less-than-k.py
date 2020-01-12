#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#
# https://leetcode.com/problems/two-sum-less-than-k/description/
#
# algorithms
# Easy (61.73%)
# Likes:    92
# Dislikes: 9
# Total Accepted:    8.6K
# Total Submissions: 14.3K
# Testcase Example:  '[34,23,1,24,75,33,54,8]\n60'
#
# Given an array A of integers and integer K, return the maximum S such that
# there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist
# satisfying this equation, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation: 
# We can use 34 and 24 to sum 58 which is less than 60.
# 
# 
# Example 2:
# 
# 
# Input: A = [10,20,30], K = 15
# Output: -1
# Explanation: 
# In this case it's not possible to get a pair sum less that 15.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i] <= 1000
# 1 <= K <= 2000
# 
# 
#
from bisect import bisect_left

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        res = -1
        A.sort()
        for i, val in enumerate(A):
            target = K - val
            target_index = bisect_left(A, target, i+1)
            if target_index != i + 1:
                res = max(res, val + A[target_index-1])
        return res

        """
        def find_largest_value_smaller_than_target(array, target, low, high):
            start = low
            while low <= high:
                mid = low + (high - low) // 2
                if array[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return array[high] if high >= start else None

        res = -1
        A.sort()
        for i, val1 in enumerate(A):
            target = K - val1
            val2 = find_largest_value_smaller_than_target(A, target, i+1, len(A)-1)
            if val2 is not None and res < val1 + val2:
                res = val1 + val2
        return res
        """
        


        

