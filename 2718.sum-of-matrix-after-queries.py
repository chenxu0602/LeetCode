#
# @lc app=leetcode id=2718 lang=python3
#
# [2718] Sum of Matrix After Queries
#

# @lc code=start

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:

        rowcol, ans, seen = [n, n], 0, [0, 0]

        for typ, idx, val in reversed(queries):
            if seen[typ] & (1 << idx):
                continue

            seen[typ] |= (1 << idx)

            ans += val * rowcol[typ]
            rowcol[typ ^ 1] -= 1

        return ans

        
# @lc code=end

