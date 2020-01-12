#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (33.45%)
# Likes:    1464
# Dislikes: 35
# Total Accepted:    142K
# Total Submissions: 421.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        dp, maxW = [[0] * (n+1) for _ in range(m+1)], 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                maxW = max(maxW, dp[i][j])

        return maxW * maxW

        
# @lc code=end

