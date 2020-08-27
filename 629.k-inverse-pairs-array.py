#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#
# https://leetcode.com/problems/k-inverse-pairs-array/description/
#
# algorithms
# Hard (31.06%)
# Likes:    325
# Dislikes: 75
# Total Accepted:    11.2K
# Total Submissions: 35.9K
# Testcase Example:  '3\n0'
#
# Given two integers n and k, find how many different arrays consist of numbers
# from 1 to n such that there are exactly k inverse pairs.
# 
# We define an inverse pair as following: For ith and jth element in the array,
# if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.
# 
# Since the answer may be very large, the answer should be modulo 10^9 + 7.
# 
# Example 1:
# 
# 
# Input: n = 3, k = 0
# Output: 1
# Explanation: 
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0
# inverse pair.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: n = 3, k = 1
# Output: 2
# Explanation: 
# The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
# 
# 
# 
# 
# Note:
# 
# 
# The integer n is in the range [1, 1000] and k is in the range [0, 1000].
# 
# 
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def __init__(self):
        self.memo = [[None] * 1001 for _ in range(1001)] 

    def kInversePairs(self, n: int, k: int) -> int:
        # Using Recursion with Memoization
        # Time  complexity: O(n^2 x k)
        # Space complexity: O(n)
        # if n == 0: return 0
        # if k == 0: return 1
        # if self.memo[n][k] is not None:
        #     return self.memo[n][k]
        # inv = 0
        # for i in range(min(k + 1, n)):
        #     inv = (inv + self.kInversePairs(n - 1, k - i)) % (10**9 + 7)
        # self.memo[n][k] = inv
        # return inv


        # @lru_cache(None)
        # def dfs(n, k):
        #     if n == 0: return 0
        #     if k == 0: return 1

        #     inv = 0
        #     for i in range(min(k + 1, n)):
        #         inv = (inv + dfs(n - 1, k - i)) % (10**9 + 7)
        #     return inv

        # return dfs(n, k)


        # Dynamic Programming
        # Time  complexity: O(n^2 x k)
        # Space complexity: O(n x k)
        # dp = [[0] * (k + 1) for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     for j in range(k + 1):
        #         if j == 0:
        #             dp[i][j] = 1
        #         else:
        #             for p in range(min(j + 1, i)):
        #                 dp[i][j] = (dp[i][j] + dp[i - 1][j - p]) % (10**9 + 7)

        # return dp[n][k]


        # Dynamic Programming with Cumulative Sum
        # Time  complexity: O(n x k)
        # Space complexity: O(n x k)
        # M = 10**9 + 7
        # dp = [[0] * (k + 1) for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     for j in range(k + 1):
        #         if j == 0:
        #             dp[i][j] = 1
        #         else:
        #             if j - i >= 0:
        #                 val = (dp[i - 1][j] + M - dp[i - 1][j - i]) % M
        #             else:
        #                 val = (dp[i - 1][j] + M) % M

        #             dp[i][j] = (dp[i][j - 1] + val) % M

        # if k > 0:
        #     return (dp[n][k] + M - dp[n][k - 1]) % M
        # else:
        #     return (dp[n][k] + M) % M


        # @lru_cache(None)
        # M = 10**9 + 7
        # def dfs(n, k):
        #     if n == 0: return 0
        #     if k == 0: return 1
        #     val = 0
        #     if k - n >= 0:
        #         val = (dfs(n-1, k) + M - dfs(n-1, k-n)) % M
        #     else:
        #         val = (dfs(n-1, k) + M) % M

        #     return (dfs(n, k-1) + val) % M
        
        # if k > 0:
        #     return (dfs(n, k) + M - dfs(n, k-1)) % M
        # else:
        #     return (dfs(n, k) + M) % M


        # 1-D Dynamic Programmming
        # Time  complexity: O(n x k)
        # Space complexity: O(k)
        M = 10**9 + 7
        dp = [0] * (k + 1)
        for i in range(1, n + 1):
            temp = [0] * (k + 1)
            temp[0] = 1
            for j in range(1, k + 1):
                val = dp[j]
                if j - i >= 0:
                    val = (dp[j] + M - dp[j - i]) % M
                temp[j] = (temp[j - 1] + val) % M
            dp = temp

        if k > 0:
            return (dp[k] + M - dp[k - 1]) % M
        else:
            return dp[k]





        
        
# @lc code=end

