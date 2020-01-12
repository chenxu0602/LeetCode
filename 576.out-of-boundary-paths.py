#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#
# https://leetcode.com/problems/out-of-boundary-paths/description/
#
# algorithms
# Medium (32.45%)
# Likes:    312
# Dislikes: 109
# Total Accepted:    18.7K
# Total Submissions: 57.5K
# Testcase Example:  '2\n2\n2\n0\n0'
#
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the
# ball, you can move the ball to adjacent cell or cross the grid boundary in
# four directions (up, down, left, right). However, you can at most move N
# times. Find out the number of paths to move the ball out of grid boundary.
# The answer may be very large, return it after mod 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
# 
# 
# 
# Example 2:
# 
# 
# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].
# 
# 
#
class Solution:

    def findPathsDFS(self, m, n, N, row, col, memo):
        if row < 0 or row >= m or col < 0 or col >= n:
            return 1

        if N == 0:
            return 0

        if memo[row][col][N] != -1:
            return memo[row][col][N]

        path = self.findPathsDFS(m, n, N-1, row-1, col, memo)  \
            + self.findPathsDFS(m, n, N-1, row, col+1, memo) \
            + self.findPathsDFS(m, n, N-1, row+1, col, memo) \
            + self.findPathsDFS(m, n, N-1, row, col-1, memo) 

        memo[row][col][N] = int(path % 1000000007)

        return memo[row][col][N]

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:

        """
        memo = [[[-1 for _ in range(N+1)] for _ in range(n)] for _ in range(m)]
        num_of_path = self.findPathsDFS(m, n, N, i, j, memo)
        return num_of_path
        """

        M = 1000000000 + 7
        dp = [[0] * n for _ in range(m)]
        dp[i][j] = 1
        count = 0

        for moves in range(1, N+1):
            temp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        count = (count + dp[i][j]) % M
                    if j == n - 1:
                        count = (count + dp[i][j]) % M
                    if i == 0:
                        count = (count + dp[i][j]) % M
                    if j == 0:
                        count = (count + dp[i][j]) % M
                    
                    temp[i][j] += dp[i-1][j] if i > 0 else 0
                    temp[i][j] += dp[i+1][j] if i < m - 1 else 0
                    temp[i][j] += dp[i][j-1] if j > 0 else 0
                    temp[i][j] += dp[i][j+1] if j < n - 1 else 0

            dp = temp

        return count

                    
        

