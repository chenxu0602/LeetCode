#
# @lc app=leetcode id=2906 lang=python3
#
# [2906] Construct Product Matrix
#

# @lc code=start
from itertools import accumulate, chain

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        MOD = 12345
        m, n = map(len, (grid, grid[0]))
        myMul = lambda x, y: (x * y) % MOD

        arr  = list(chain(*grid))
        pref = list(accumulate(arr,       myMul, initial=1))
        suff = list(accumulate(arr[::-1], myMul, initial=1))[::-1]

        ans = [p * s % MOD for p, s in zip(pref, suff[1:])]

        return list(zip(*[iter(ans)] * n))
        
# @lc code=end

