#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/
#
# algorithms
# Medium (62.67%)
# Likes:    288
# Dislikes: 34
# Total Accepted:    8.9K
# Total Submissions: 14.2K
# Testcase Example:  '[1,15,7,9,2,5,10]\n3'
#
# Given an integer array A, you partition the array into (contiguous) subarrays
# of length at most K.  After partitioning, each subarray has their values
# changed to become the maximum value of that subarray.
# 
# Return the largest sum of the given array after partitioning.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,15,7,9,2,5,10], K = 3
# Output: 84
# Explanation: A becomes [15,15,15,9,10,10,10]
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= A.length <= 500
# 0 <= A[i] <= 10^6
# 
# 
#
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:

        N = len(A)
        dp = [0] * (N + 1)

        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N-1]

        

