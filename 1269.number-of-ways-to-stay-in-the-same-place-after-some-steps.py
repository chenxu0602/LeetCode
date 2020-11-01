#
# @lc app=leetcode id=1269 lang=python3
#
# [1269] Number of Ways to Stay in the Same Place After Some Steps
#
# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/description/
#
# algorithms
# Hard (40.86%)
# Likes:    131
# Dislikes: 7
# Total Accepted:    5.6K
# Total Submissions: 13.8K
# Testcase Example:  '3\n2'
#
# You have a pointer at index 0 in an array of size arrLen. At each step, you
# can move 1 position to the left, 1 position to the right in the array or stay
# in the same place  (The pointer should not be placed outside the array at any
# time).
# 
# Given two integers steps and arrLen, return the number of ways such that your
# pointer still at index 0 after exactly steps steps.
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
# 
# 
# Example 2:
# 
# 
# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay
# 
# 
# Example 3:
# 
# 
# Input: steps = 4, arrLen = 2
# Output: 8
# 
# 
# 
# Constraints:
# 
# 
# 1 <= steps <= 500
# 1 <= arrLen <= 10^6
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        # @lru_cache(None)
        # def dfs(i, pos):
        #     if i == steps: return pos == 0
        #     if pos < 0 or pos >= arrLen:
        #         return 0
        #     return (dfs(i + 1, pos) + dfs(i + 1, pos - 1) + dfs(i + 1, pos + 1)) % MOD

        # return dfs(0, 0)


        A = [0, 1]
        r = min(arrLen, steps // 2 + 1)
        for t in range(steps):
            A[1:] = [sum(A[i - 1:i + 2]) % MOD for i in range(1, min(r + 1, t + 3))]
        return A[1] % MOD
        
# @lc code=end

