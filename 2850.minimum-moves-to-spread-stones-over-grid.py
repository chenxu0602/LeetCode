#
# @lc app=leetcode id=2850 lang=python3
#
# [2850] Minimum Moves to Spread Stones Over Grid
#

# @lc code=start
from itertools import product, permutations

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        zeros, spare = [], []

        for i, j in product(range(3), range(3)):
            stone = grid[i][j]
            if stone == 0: zeros += (i, j),
            if stone > 1:  spare.extend([(i, j)] * (stone - 1))

        return min((sum(map(dist, zeros, per))) for per in set(permutations(spare)))
        
# @lc code=end

