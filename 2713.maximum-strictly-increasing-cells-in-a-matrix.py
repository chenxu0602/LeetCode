#
# @lc app=leetcode id=2713 lang=python3
#
# [2713] Maximum Strictly Increasing Cells in a Matrix
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:

        m, n = map(len, (mat, mat[0]))
        A = defaultdict(list)
        for i in range(m):
            for j in range(n):
                A[mat[i][j]].append([i, j])

        dp = [[0] * n for _ in range(m)]

        # we use res[i] to record the maximum step for row i,
        # we use res[m + j] to record the maximum step for col j.
        res = [0] * (m + n)

        for a in sorted(A):
            for i, j in A[a]:
                dp[i][j] = max(res[i], res[~j]) + 1

            for i, j in A[a]:
                res[~j] = max(res[~j], dp[i][j])
                res[i] = max(res[i], dp[i][j])

        return max(res)

        
# @lc code=end

