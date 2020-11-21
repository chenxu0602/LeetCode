#
# @lc app=leetcode id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/
#
# algorithms
# Hard (53.37%)
# Likes:    261
# Dislikes: 9
# Total Accepted:    7.2K
# Total Submissions: 13.6K
# Testcase Example:  '["A..","AAA","..."]\n3'
#
# Given a rectangular pizza represented as a rows x cols matrix containing the
# following characters: 'A' (an apple) and '.' (empty cell) and given the
# integer k. You have to cut the pizza into k pieces using k-1 cuts. 
# 
# For each cut you choose the direction: vertical or horizontal, then you
# choose a cut position at the cell boundary and cut the pizza into two pieces.
# If you cut the pizza vertically, give the left part of the pizza to a person.
# If you cut the pizza horizontally, give the upper part of the pizza to a
# person. Give the last piece of pizza to the last person.
# 
# Return the number of ways of cutting the pizza such that each piece contains
# at least one apple. Since the answer can be a huge number, return this modulo
# 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: pizza = ["A..","AAA","..."], k = 3
# Output: 3 
# Explanation: The figure above shows the three ways to cut the pizza. Note
# that pieces must contain at least one apple.
# 
# 
# Example 2:
# 
# 
# Input: pizza = ["A..","AA.","..."], k = 3
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: pizza = ["A..","A..","..."], k = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= rows, cols <= 50
# rows == pizza.length
# cols == pizza[i].length
# 1 <= k <= 10
# pizza consists of characters 'A' and '.' only.
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # Time  complexity: O(kmn(m + n))
        # Space complexity: O(kmn)
        m, n = map(len, (pizza, pizza[0]))
        MOD = 10**9 + 7

        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                preSum[r][c] = preSum[r][c + 1] + preSum[r + 1][c] - preSum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(l, r, c):
            if preSum[r][c] == 0:
                return 0
            if l == 0:
                return 1

            ans = 0

            for nr in range(r + 1, m):
                if preSum[r][c] - preSum[nr][c] > 0:
                    ans = (ans + dp(l - 1, nr, c)) % MOD

            for nc in range(c + 1, n):
                if preSum[r][c] - preSum[r][nc] > 0:
                    ans = (ans + dp(l - 1, r, nc)) % MOD

            return ans

        return dp(k - 1, 0, 0)
        
# @lc code=end

