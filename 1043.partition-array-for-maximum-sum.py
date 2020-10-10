#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/
#
# algorithms
# Medium (63.52%)
# Likes:    426
# Dislikes: 59
# Total Accepted:    13.1K
# Total Submissions: 20.6K
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

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        # O(N x K)
        # Choose the maximum from the following combinations:
        # dp_sum[X - 1] + max(A[X]) x 1
        # dp_sum[X - 2] + max(A[X-1], A[X]) x 2
        # dp_sum[X - 3] + max(A[X-2], A[X-1], A[X]) x 3
        # ...
        # dp_sum[X - (k-1)] + max(A[X-(k-2)] ..... A[X]) x (k-1)
        # dp_sum[X - k] + max(A[X-(k-1)] ..... A[X]) x k
        dp_sum = [0 for _ in range(len(A))]
        dp_sum[0] = A[0]
        max_so_far = A[0]
        for i in range(1, K):
            max_so_far = max(max_so_far, A[i])
            dp_sum[i] = (i + 1) * max_so_far

        for i in range(K, len(dp_sum)):
            partition_max = 0
            for back in range(K):
                partition_max = max(partition_max, A[i - back])
                prev_sum = dp_sum[i - back - 1]
                dp_sum[i] = max(dp_sum[i], prev_sum + partition_max * (back + 1))

        return dp_sum[-1]


        # n = len(A)
        # dp = [0] * n

        # for i in range(n):
        #     curMax = 0
        #     for k in range(1, min(K, i + 1) + 1):
        #         curMax = max(curMax, A[i - k + 1])
        #         dp[i] = max(dp[i], dp[i - k] + curMax * k if i >= k else curMax * k)
        
        # return dp[-1]


# @lc code=end

