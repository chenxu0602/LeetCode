#
# @lc app=leetcode id=2711 lang=python3
#
# [2711] Difference of Number of Distinct Values on Diagonals
#

# @lc code=start
from collections import defaultdict
from itertools import product

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:

        d = defaultdict(list)

        for i, j in product(range(len(grid)), range(len(grid[0]))):
            d[i - j].append((i, j))

        for diag in d:
            arr = [grid[i][j] for i, j in d[diag]]

            for idx, (i, j) in enumerate(d[diag]):
                grid[i][j] = abs(len(set(arr[:idx])) - len(set(arr[idx + 1:])))

        return grid
        
# @lc code=end

