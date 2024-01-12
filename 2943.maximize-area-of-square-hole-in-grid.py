#
# @lc app=leetcode id=2943 lang=python3
#
# [2943] Maximize Area of Square Hole in Grid
#

# @lc code=start
from itertools import pairwise 

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        def find_max(bars):
            bars.sort()
            s = ''.join([str(int(y - x == 1)) for x, y in pairwise(bars)])
            return max(map(len, s.split('0'))) + 2

        return pow(min(find_max(hBars), find_max(vBars)), 2)
        
# @lc code=end

