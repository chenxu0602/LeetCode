#
# @lc app=leetcode id=3343 lang=python3
#
# [3343] Count Number of Balanced Permutations
#

# @lc code=start
from collections import Counter
from functools import lru_cache
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        cnt = Counter(map(int, num))
        total = sum(map(int, num))

        @lru_cache(None)
        def dfs(i, odd, even, balance):
            if odd == 0 and even == 0 and balance == 0:
                return 1
            if i < 0 or odd < 0 or even < 0 or balance < 0:
                return 0

            res = 0
            for j in range(0, cnt[i] + 1):
                res += comb(odd, j) * comb(even, cnt[i] - j) * dfs(i - 1, odd - j, even - cnt[i] + j, balance - i * j)
            return res % MOD

        return 0 if total % 2 else dfs(9, len(num) - len(num) // 2, len(num) // 2, total // 2)

        
# @lc code=end

