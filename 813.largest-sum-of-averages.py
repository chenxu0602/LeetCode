#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#
# https://leetcode.com/problems/largest-sum-of-averages/description/
#
# algorithms
# Medium (46.20%)
# Likes:    602
# Dislikes: 22
# Total Accepted:    15.5K
# Total Submissions: 33.5K
# Testcase Example:  '[9,1,2,3,9]\n3'
#
# We partition a row of numbers A into at most K adjacent (non-empty) groups,
# then our score is the sum of the average of each group. What is the largest
# score we can achieve?
# 
# Note that our partition must use every number in A, and that scores are not
# necessarily integers.
# 
# 
# Example:
# Input: 
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation: 
# The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 +
# (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= A.length <= 100.
# 1 <= A[i] <= 10000.
# 1 <= K <= A.length.
# Answers within 10^-6 of the correct answer will be accepted as correct.
# 
# 
#
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        """
        P = [0] 
        for x in A:
            P.append(P[-1] + x)

        def average(i, j):
            return (P[j] - P[i]) / float(j - i)

        N = len(A)
        dp = [average(i, N) for i in range(N)]

        for k in range(K-1):
            for i in range(N):
                for j in range(i+1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]
        """

        dp = [[0 for _ in range(len(A))] for _ in range(K)]
        cur_sum = 0

        for j in range(len(A)):
            cur_sum += A[j]
            dp[0][j] = float(cur_sum) / (j + 1)

        for i in range(1, K):
            for j in range(len(A)):
                cur_sum = 0
                for k in range(j, i - 1, -1):
                    cur_sum += A[k]
                    dp[i][j] = max(dp[i][j], dp[i-1][k-1] + float(cur_sum) / (j - k + 1))
        return dp[-1][-1]


