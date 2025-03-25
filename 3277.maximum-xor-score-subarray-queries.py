#
# @lc app=leetcode id=3277 lang=python3
#
# [3277] Maximum XOR Score Subarray Queries
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        """
        n = len(nums)
        xor = [nums[:] for _ in range(n)]
        score = [nums[:] for _ in range(n)]

        for d in range(1, n):
            for i in range(n - d):
                j = i + d
                xor[i][j] = xor[i][j - 1] ^ xor[i + 1][j]
                score[i][j] = max(score[i][j - 1], score[i + 1][j], xor[i][j])

        return [score[i][j] for i, j in queries]
        """


        """
        @lru_cache(None)
        def dp(i, j):
            if i == j: return [nums[i]] * 2
            xor1, score1 = dp(i, j - 1)
            xor2, score2 = dp(i + 1, j)
            return [xor1 ^ xor2, max(xor1 ^ xor2, score1, score2)]

        return [dp(*q)[1] for q in queries]
        """


        n = len(nums)
        f = [[0] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            mx[i][i] = f[i][i] = nums[i]
            for j in range(i + 1, n):
                f[i][j] = f[i][j - 1] ^ f[i + 1][j]
                mx[i][j] = max(f[i][j], mx[i + 1][j], mx[i][j - 1])

        return [mx[l][r] for l, r in queries]

        
# @lc code=end

