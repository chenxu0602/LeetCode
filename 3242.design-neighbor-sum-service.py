#
# @lc app=leetcode id=3242 lang=python3
#
# [3242] Design Neighbor Sum Service
#

# @lc code=start
from collections import defaultdict
from itertools import product

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.indices = defaultdict(tuple)
        self.values  = defaultdict(int)

        m, n = map(len, (grid, grid[0]))

        for i, j in product(range(m), range(n)):
            self.values[(i, j)] = grid[i][j]
            self.indices[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:

        sum_ = 0

        i, j = self.indices[value]
        for I, J in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
            if (I, J) in self.values:
                sum_ += self.values[(I, J)]

        return sum_
        

    def diagonalSum(self, value: int) -> int:

        sum_ = 0

        i, j = self.indices[value]
        for I, J in (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1), (i + 1, j + 1):
            if (I, J) in self.values:
                sum_ += self.values[(I, J)]

        return sum_
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
# @lc code=end

