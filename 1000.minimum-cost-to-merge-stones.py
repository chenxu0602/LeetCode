#
# @lc app=leetcode id=1000 lang=python3
#
# [1000] Minimum Cost to Merge Stones
#
# https://leetcode.com/problems/minimum-cost-to-merge-stones/description/
#
# algorithms
# Hard (34.16%)
# Likes:    291
# Dislikes: 23
# Total Accepted:    6.4K
# Total Submissions: 17.8K
# Testcase Example:  '[3,2,4,1]\n2'
#
# There are N piles of stones arranged in a row.  The i-th pile has stones[i]
# stones.
# 
# A move consists of merging exactly K consecutive piles into one pile, and the
# cost of this move is equal to the total number of stones in these K piles.
# 
# Find the minimum cost to merge all piles of stones into one pile.  If it is
# impossible, return -1.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: stones = [3,2,4,1], K = 2
# Output: 20
# Explanation: 
# We start with [3, 2, 4, 1].
# We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
# We merge [4, 1] for a cost of 5, and we are left with [5, 5].
# We merge [5, 5] for a cost of 10, and we are left with [10].
# The total cost was 20, and this is the minimum possible.
# 
# 
# 
# Example 2:
# 
# 
# Input: stones = [3,2,4,1], K = 3
# Output: -1
# Explanation: After any merge operation, there are 2 piles left, and we can't
# merge anymore.  So the task is impossible.
# 
# 
# 
# Example 3:
# 
# 
# Input: stones = [3,5,1,2,6], K = 3
# Output: 25
# Explanation: 
# We start with [3, 5, 1, 2, 6].
# We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
# We merge [3, 8, 6] for a cost of 17, and we are left with [17].
# The total cost was 25, and this is the minimum possible.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= stones.length <= 30
# 2 <= K <= 30
# 1 <= stones[i] <= 100
# 
# 
# 
# 
#
from functools import lru_cache

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        
        """
        def recursive(i, j, piles):
            if i == j and piles == 1:
                return 0

            if (j - i + 1 - piles) % (K - 1) != 0:
                return float("inf")

            if (i, j, piles) in dp:
                return dp[(i, j, piles)]

            if piles == 1:
                dp[(i, j, piles)] = recursive(i, j, K) + pre_sum[j+1] - pre_sum[i]
                return dp[(i, j, piles)]
            else:
                min_cost = float("inf")
                for k in range(i, j, K-1):
                    min_cost = min(min_cost, recursive(i, k, 1) + recursive(k+1, j, piles-1))
                dp[(i, j, piles)] = min_cost
                return dp[(i, j, piles)]

        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + stones[i]
        dp = {}
        return recursive(0, n-1, 1)
        """

        """
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]

        @lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return float("inf")
            if i == j:
                return 0 if m == 1 else float("inf")
            if m == 1:
                return dp(i, j, K) + prefix[j+1] - prefix[i]

            return min(dp(i, mid, 1) + dp(mid+1, j, m-1) for mid in range(i, j, K-1))
        res = dp(0, n-1, 1)
        return res if res < float("inf") else -1
        """

        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]

        @lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K:
                return 0
            res = min(dp(i, mid) + dp(mid+1, j) for mid in range(i, j, K-1))
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]

            return res

        return dp(0, n-1)
        

