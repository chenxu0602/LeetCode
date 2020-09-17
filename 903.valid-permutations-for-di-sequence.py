#
# @lc app=leetcode id=903 lang=python3
#
# [903] Valid Permutations for DI Sequence
#
# https://leetcode.com/problems/valid-permutations-for-di-sequence/description/
#
# algorithms
# Hard (49.50%)
# Likes:    300
# Dislikes: 28
# Total Accepted:    6.1K
# Total Submissions: 12.1K
# Testcase Example:  '"DID"'
#
# We are given S, a length n string of characters from the set {'D', 'I'}.
# (These letters stand for "decreasing" and "increasing".)
# 
# A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1,
# ..., n}, such that for all i:
# 
# 
# If S[i] == 'D', then P[i] > P[i+1], and;
# If S[i] == 'I', then P[i] < P[i+1].
# 
# 
# How many valid permutations are there?  Since the answer may be large, return
# your answer modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: "DID"
# Output: 5
# Explanation: 
# The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 200
# S consists only of characters from the set {'D', 'I'}.
# 
# 
# 
# 
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        # Dynamic Programming
        # Time  complexity: O(N^3)
        # Space complexity: O(N^2)
        # MOD = 10**9 + 7
        # N = len(S)

        # @lru_cache(None)
        # def dp(i, j):
        #     # How many ways to place P_i with relative rank j?
        #     if i == 0:
        #         return 1
        #     elif S[i - 1] == 'D':
        #         return sum(dp(i - 1, k) for k in range(j, i)) % MOD
        #     else:
        #         return sum(dp(i - 1, k) for k in range(j))

        # return sum(dp(N, j) for j in range(N + 1)) % MOD

        
        # Time  complexity: O(N^2)
        # Space complexity: O(N^2)
        # MOD = 10**9 + 7
        # N = len(S)

        # @lru_cache(None)
        # def dp(i, j):
        #     if not 0 <= j <= i:
        #         return 0
        #     if i == 0:
        #         return 1
        #     elif S[i - 1] == 'D':
        #         return (dp(i, j + 1) + dp(i - 1, j)) % MOD
        #     else:
        #         return (dp(i, j - 1) + dp(i - 1, j - 1)) % MOD

        # return sum(dp(N, j) for j in range(N + 1)) % MOD


        # Divide and Conquer
        # Time  complexity: O(N^2)
        # Space complexity: O(N^2)
        # MOD = 10**9 + 7

        # fac = [1, 1]
        # for x in range(2, 201):
        #     fac.append(fac[-1] * x % MOD)
        # facinv = [pow(f, MOD - 2, MOD) for f in fac]

        # def binom(n, k):
        #     return fac[n] * facinv[n - k] % MOD * facinv[k] % MOD

        # @lru_cache(None)
        # def dp(i, j):
        #     if i >= j: return 1
        #     ans = 0
        #     n = j - i + 2
        #     if S[i] == 'I': ans += dp(i + 1, j)
        #     if S[j] == 'D': ans += dp(i, j - 1)

        #     for k in range(i + 1, j + 1):
        #         if S[k - 1:k + 1] == 'DI':
        #             ans += binom(n - 1, k - i) * dp(i, k - 2) % MOD * dp(k + 1, j) % MOD
        #             ans %= MOD
        #     return ans

        # return dp(0, len(S) - 1)

        # MOD = 10**9 + 7

        # dp = [1] * (len(S) + 1)
        # for c in S:
        #     if c == 'I':
        #         dp = dp[:-1]
        #         for i in range(1, len(dp)):
        #             dp[i] += dp[i - 1]
        #     else:
        #         dp = dp[1:]
        #         for i in range(len(dp) - 1)[::-1]:
        #             dp[i] += dp[i + 1]

        # return dp[0] % MOD


        import itertools
        MOD = 10**9 + 7
        dp = [1] * (len(S) + 1)
        for a, b in zip('I' + S, S):
            dp = list(itertools.accumulate(dp[:-1] if a == b else dp[-1:0:-1]))
        return dp[0] % MOD

# @lc code=end

