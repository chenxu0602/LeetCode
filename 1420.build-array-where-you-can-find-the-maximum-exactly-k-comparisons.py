#
# @lc app=leetcode id=1420 lang=python3
#
# [1420] Build Array Where You Can Find The Maximum Exactly K Comparisons
#
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/description/
#
# algorithms
# Hard (64.35%)
# Likes:    235
# Dislikes: 5
# Total Accepted:    6.3K
# Total Submissions: 9.8K
# Testcase Example:  '2\n3\n1'
#
# Given three integers n, m and k. Consider the following algorithm to find the
# maximum element of an array of positive integers:
# 
# You should build the array arr which has the following properties:
# 
# 
# arr has exactly n integers.
# 1 <= arr[i] <= m where (0 <= i < n).
# After applying the mentioned algorithm to arr, the value search_cost is equal
# to k.
# 
# 
# Return the number of ways to build the array arr under the mentioned
# conditions. As the answer may grow large, the answer must be computed modulo
# 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 2, m = 3, k = 1
# Output: 6
# Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2]
# [3, 3]
# 
# 
# Example 2:
# 
# 
# Input: n = 5, m = 2, k = 3
# Output: 0
# Explanation: There are no possible arrays that satisify the mentioned
# conditions.
# 
# 
# Example 3:
# 
# 
# Input: n = 9, m = 1, k = 1
# Output: 1
# Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
# 
# 
# Example 4:
# 
# 
# Input: n = 50, m = 100, k = 25
# Output: 34549172
# Explanation: Don't forget to compute the answer modulo 1000000007
# 
# 
# Example 5:
# 
# 
# Input: n = 37, m = 17, k = 7
# Output: 418930126
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 50
# 1 <= m <= 100
# 0 <= k <= n
# 
#

# @lc code=start
import itertools

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # dp[i][j][k] means the number of ways for array with length i, number of cost is j and max value is k.
        N, M, K = n, m, k
        dp = [[[0] * (M + 1) for _ in range(K + 1)] for _ in range(N + 1)]

        for k in range(1, M + 1):
            dp[1][1][k] = 1

        for i, j, k in itertools.product(range(1, N + 1), range(1, K + 1), range(M + 1)):
            dp[i][j][k] += dp[i - 1][j][k] * k
            dp[i][j][k] += sum(dp[i - 1][j - 1][1:k])

        return sum(dp[N][K][1:]) % (10**9 + 7)

        
# @lc code=end

