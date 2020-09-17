#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#
# https://leetcode.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (25.01%)
# Likes:    455
# Dislikes: 46
# Total Accepted:    9.5K
# Total Submissions: 37.4K
# Testcase Example:  '1\n2'
#
# You are given K eggs, and you have access to a building with N floors from 1
# to N. 
# 
# Each egg is identical in function, and if an egg breaks, you cannot drop it
# again.
# 
# You know that there exists a floor F with 0 <= F <= N such that any egg
# dropped at a floor higher than F will break, and any egg dropped at or below
# floor F will not break.
# 
# Each move, you may take an egg (if you have an unbroken one) and drop it from
# any floor X (with 1 <= X <= N). 
# 
# Your goal is to know with certainty what the value of F is.
# 
# What is the minimum number of moves that you need to know with certainty what
# F is, regardless of the initial value of F?
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: K = 1, N = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty
# that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with
# certainty.
# 
# 
# 
# Example 2:
# 
# 
# Input: K = 2, N = 6
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: K = 3, N = 14
# Output: 4
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= 100
# 1 <= N <= 10000
# 
# 
# 
# 
# 
#
from functools import lru_cache

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # Dynamic Programming with Binary Search
        # K eggs and N floors left. When we drop an egg from floor X, it either survives and we have state (K, N-X), or it breaks and we have state (K-1, X-1).
        # This approach would lead to a O(K x N^2) algorithm, but this is not efficient enough for the given constraints. 
        # dp(K-1, X-1) is an increasing function on X while dp(K, N-X) is a decreasing function on X.
        # dp(K, N) = min_{1<=X<=N} (max(dp(K-1, X-1), dp(K, N-X))) means we don't need to check every X to find the minimum.
        # Time  complexity: O(K x NlogN)
        # Space complexity: O(K x N)
        # @lru_cache(None)
        # def dp(k, n):
        #     if n == 0:
        #         ans = 0
        #     elif k == 1:
        #         ans = n
        #     else:
        #         lo, hi = 1, n
        #         # keep a gap of 2 X values to manually check later
        #         while lo + 1 < hi:
        #             x = (lo + hi) // 2
        #             t1 = dp(k - 1, x - 1)
        #             t2 = dp(k, n - x)

        #             if t1 < t2:
        #                 lo = x
        #             elif t1 > t2:
        #                 hi = x
        #             else:
        #                 lo = hi = x

        #         ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (lo, hi))

        #     return ans

        # return dp(K, N)


        # Dynamic Programming with Optimality Criterion
        # Time  complexity: O(K x N)
        # Space complexity: O(N)
        # Right now, dp[i] represents dp(1, i)
        # dp = list(range(N + 1))
        # for k in range(2, K + 1):
        #     # Now, we will develop dp2[i] = dp(k, i)
        #     dp2 = [0]
        #     x = 1
        #     for n in range(1, N + 1):
        #         # Let's find dp2[n] = dp(k, n)
        #         # Increase our optimal x while we can make our answer better.
        #         # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
        #         # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
        #         while x < n and max(dp[x - 1], dp2[n - x]) > max(dp[x] ,dp2[n - x - 1]):
        #             x += 1

        #         # The final answer happens at this x.
        #         dp2.append(1 + max(dp[x - 1], dp2[n - x]))

        #     dp = dp2

        # return dp[-1]


        # Mathematical
        # f(T, K) = 1 + f(T-1, K-1) + f(T-1, K)
        # f(T, K-1) = 1 + f(T-1, K-2) + f(T-1, K-1)
        # g(t,k) = f(t,k) - f(t, k-1) = g(t-1, k) + g(t-1, k-1) = C(t, k+1)
        # f(t, k) = sum_{1<=x<=K} g(t, x) = sum_(0<=x<=K) C(t, x)
        # Binary search for t that satisfies f(t, K) >= N.
        # Time  complexity: O(K x logN)
        # Space complexity: O(1)
        # def f(x):
        #     ans, r = 0, 1
        #     for i in range(1, K + 1):
        #         r *= x - i + 1
        #         r //= i
        #         ans += r
        #         if ans >= N: break
        #     return ans

        # lo, hi = 1, N
        # while lo < hi:
        #     mi = (lo + hi) // 2
        #     if f(mi) < N:
        #         lo = mi + 1
        #     else:
        #         hi = mi
        # return lo


        # dp[k][m] means that given k eggs and m moves, the max number of floor that we can cover.
        # dp[k][m] = 1 + dp[k-1][m-1] + dp[k][m-1]
        # we take 1 move to a floor, if the egg breaks, we can check dp[k-1][m-1] floors,
        # if the egg doesn't, we can check dp[k][m-1] floors.
        # dp = [[0] * (N + 1) for _ in range(K + 1)]
        # for m in range(1, N + 1):
        #     for k in range(1, K + 1):
        #         dp[k][m] = 1 + dp[k - 1][m - 1] + dp[k][m - 1]
        #     if dp[k][m] >= N: 
        #         return m

        # 1-D version
        # dp = [0, 0]
        # m = 0
        # while dp[-1] < N:
        #     for i in range(len(dp) - 1, 0, -1):
        #         dp[i] += 1 + dp[i - 1]
        #     if len(dp) < K + 1:
        #         dp.append(dp[-1]) 
        #     m += 1
        # return m


        # Let floors[i] be the number of floors that can be checked with i eggs
        # O(K x logN)
        drops = 0
        floors = [0] * (K + 1)
        while floors[K] < N:
            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
            print(floors)
            drops += 1
        return drops



