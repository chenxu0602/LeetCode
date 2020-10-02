#
# @lc app=leetcode id=1000 lang=python3
#
# [1000] Minimum Cost to Merge Stones
#
# https://leetcode.com/problems/minimum-cost-to-merge-stones/description/
#
# algorithms
# Hard (39.61%)
# Likes:    624
# Dislikes: 45
# Total Accepted:    15K
# Total Submissions: 37.8K
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

# @lc code=start
from functools import lru_cache
import itertools

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        # dp[i][j] means the minimum cost needed to merge stones[i] ~ stones[j].
        # Time  complexity: O(N^3 / K)
        # Space complexity: O(KN^2)
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        @lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: return 0

            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))

            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]

            return res

        return dp(0, n - 1)
        
# @lc code=end

