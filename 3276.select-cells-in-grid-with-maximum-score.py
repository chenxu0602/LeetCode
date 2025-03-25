#
# @lc app=leetcode id=3276 lang=python3
#
# [3276] Select Cells in Grid With Maximum Score
#

# @lc code=start
from functools import lru_cache
from collections import defaultdict

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(i, mask):
            nonlocal values
            if i == len(values): return 0
            cur, val = mask, values[i]

            bits, j, res = d[val], 0, 0

            for _ in range(bits.bit_length()):
                if (bits % 2, cur % 2) == (1, 0):
                    res = max(res, val + dp(i + 1, mask | (1 << j)))

                j, bits, cur = j + 1, bits // 2, cur // 2

            if not res: res = dp(i + 1, mask)

            return res


        d = defaultdict(int) 
        for i, row in enumerate(grid):
            for num in row:
                d[num] |= (1 << i)

        values = sorted(d, reverse=True)
        return dp(0, 0)

        
# @lc code=end

