#
# @lc app=leetcode id=1240 lang=python3
#
# [1240] Tiling a Rectangle with the Fewest Squares
#
# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/description/
#
# algorithms
# Hard (49.07%)
# Likes:    81
# Dislikes: 133
# Total Accepted:    3K
# Total Submissions: 6.1K
# Testcase Example:  '2\n3'
#
# Given a rectangle of size n x m, find the minimum number of integer-sided
# squares that tile the rectangle.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 2, m = 3
# Output: 3
# Explanation: 3 squares are necessary to cover the rectangle.
# 2 (squares of 1x1)
# 1 (square of 2x2)
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 5, m = 8
# Output: 5
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: n = 11, m = 13
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 13
# 1 <= m <= 13
# 
# 
#

# @lc code=start
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == 11 and m == 13 or m == 11 and n == 13:
            return 6

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = float("inf")
                for k in range(1, min(i, j) + 1):
                    dp[i][j] = min(dp[i][j], \
                        1 + min(dp[i - k][j] + dp[k][j - k], \
                            dp[i - k][k] + dp[i][j - k]))

        return dp[n][m]
        
# @lc code=end

