#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = Counter(zip(*grid))
        return sum(count[tuple(row)] for row in grid)
        
# @lc code=end

