#
# @lc app=leetcode id=920 lang=python3
#
# [920] Number of Music Playlists
#
# https://leetcode.com/problems/number-of-music-playlists/description/
#
# algorithms
# Hard (45.47%)
# Likes:    317
# Dislikes: 36
# Total Accepted:    8.7K
# Total Submissions: 19.1K
# Testcase Example:  '3\n3\n1'
#
# Your music player contains N different songs and she wants to listen to L
# (not necessarily different) songs during your trip.  You create a playlist so
# that:
# 
# 
# Every song is played at least once
# A song can only be played again only if K other songs have been played
# 
# 
# Return the number of possible playlists.  As the answer can be very large,
# return it modulo 10^9 + 7.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: N = 3, L = 3, K = 1
# Output: 6
# Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3],
# [2, 3, 1], [3, 1, 2], [3, 2, 1].
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 2, L = 3, K = 0
# Output: 6
# Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1],
# [2, 2, 1], [2, 1, 2], [1, 2, 2]
# 
# 
# 
# Example 3:
# 
# 
# Input: N = 2, L = 3, K = 1
# Output: 2
# Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= K < N <= L <= 100
# 
# 
# 
# 
#

# @lc code=start
from functools import lru_cache
from math import factorial

class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        # Dynamic Programming
        # Let dp[i][j] be the number of playlists of length i that have exactly j unique songs.
        # Last song, we either played a song for the first time or we didn't. 
        # If we did, then we had dp[i-1][j-1] * (N-j) ways to choose it. 
        # If we didn't, then we repeated a previous song in dp[i-1][j] * max(j-K, 0) 
        # ways (j of them, except the last K ones played are banned.)
        # Time  complexity: O(NL)
        # Space complexity: O(NL)
        # @lru_cache(None)
        # def dp(i, j):
        #     if i == 0:
        #         return +(j == 0)
        #     ans = dp(i - 1, j - 1) * (N - j + 1)
        #     ans += dp(i - 1, j) * max(j - K, 0)
        #     return ans % (10**9 + 7)

        # return dp(L, N)


        # dp = [[0] * (N + 1) for _ in range(L + 1)]
        # dp[0][0] = 1

        # for j in range(1, N + 1):
        #     for i in range(1, L + 1):
        #         dp[i][j] = dp[i - 1][j - 1] * (N - j + 1) + dp[i - 1][j] * max(j - K, 0)
        #         dp[i][j] %= (10**9 + 7)
        # return dp[L][N] % (10**9 + 7)


        dp = [[0] * (L + 1) for _ in range(N + 1)]
        for i in range(K + 1, N + 1):
            for j in range(i, L + 1):
                if i == j or i == K + 1:
                    dp[i][j] = factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - K)

        return dp[N][L] % (10**9 + 7)


        # Partitions + Dynamic Programming
        # Time  complexity: O(NL)
        # Space compleixty: O(L)
        # dp = [1] * (L - N + 1)
        # for p in range(2, N - K + 1):
        #     for i in range(1, L - N + 1):
        #         dp[i] += dp[i - 1] * p

        # ans = dp[-1]
        # for k in range(2, N + 1):
        #     ans *= k
        # return ans % (10**9 + 7)


        # Generating Functions
        # Time  complexity: O(N x logL)
        # Space complexity: O(1)
        # MOD = 10**9 + 7
        # def inv(x):
        #     return pow(x, MOD - 2, MOD)

        # C = 1
        # for x in range(1, N - K):
        #     C *= -x
        #     C %= MOD
        # C = inv(C)

        # ans = 0
        # for k in range(1, N - K + 1):
        #     ans += pow(k, L - K - 1, MOD) * C
        #     C = C * (k - (N - K)) % MOD * inv(k) % MOD

        # for k in range(1, N + 1):
        #     ans = ans * k % MOD
        # return ans

        
# @lc code=end

