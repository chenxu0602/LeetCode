#
# @lc app=leetcode id=3225 lang=python3
#
# [3225] Maximum Score From Grid Operations
#

# @lc code=start
from itertools import accumulate

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:

        # Time  complexity: O(N^3)
        # Space complexity: O(N)

        # n = len(grid)
        # prev_col_w, prev_col_wo = [0] * (n + 1), [0] * (n + 1)
        # if n == 1: return 0

        # for j in range(1, n): # loop over columns
        #     cur_col_w, cur_col_wo = [0] * (n + 1), [0] * (n + 1)
        #     for i in range(n + 1):
        #         pre_col_val, cur_col_val = 0, 0
        #         for p in range(i):
        #             cur_col_val += grid[p][j]
        #         for k in range(n + 1):
        #             if k > 0 and k <= i:
        #                 cur_col_val -= grid[k - 1][j]
        #             if k > i:
        #                 pre_col_val += grid[k - 1][j - 1]

        #             cur_col_wo[k] = max(cur_col_wo[k], pre_col_val + prev_col_wo[i])
        #             cur_col_wo[k] = max(cur_col_wo[k], prev_col_w[i])
        #             cur_col_w[k]  = max(cur_col_w[k], cur_col_val + prev_col_w[i])
        #             cur_col_w[k]  = max(cur_col_w[k], cur_col_val + pre_col_val + prev_col_wo[i])

        #     prev_col_w  = cur_col_w
        #     prev_col_wo = cur_col_wo

        # return max(prev_col_w)


        # For fixed column c:
        # dp[k] is max score of grid A[..][..c] where last column c has k black cells, and not including scores from column c.
        # ep[k] same as dp[k] but including scores from column c.

        # Glossary:
        # pb, cb : previous / current number of black cells
        # pv, cv : previous / current value (total score of columns j-1 and j)
        # pdp, pep : previous values of dp, ep.

        n = len(grid)
        acc = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        pdp, pep, ep = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        for j in range(1, n):
            dp, ep = [0] * (n + 1), [0] * (n + 1)
            for pb in range(n + 1):
                for cb in range(n + 1):
                    pv = acc[j - 1][cb] - acc[j - 1][pb] if cb > pb else 0
                    cv = acc[j][pb] - acc[j][cb] if cb < pb else 0
                    dp[cb] = max(dp[cb], pv + pdp[pb], pep[pb])
                    ep[cb] = max(ep[cb], cv + pep[pb], cv + pv + pdp[pb])

            pdp, pep = dp, ep

        return max(ep)


        
# @lc code=end

