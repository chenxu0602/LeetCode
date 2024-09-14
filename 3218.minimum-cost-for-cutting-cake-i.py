#
# @lc app=leetcode id=3218 lang=python3
#
# [3218] Minimum Cost for Cutting Cake I
#

# @lc code=start
from heapq import heappush, heappop, heapify

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:

        # The cuts should be taken, whether vertical or horizontal, 
        # in the descending order of cost with no preference to horizontal or vertical on ties. 
        # (This fact allows us to use one heap, with a boolean to keep track of each cut's dimension.)
        # Each cut in a dimension increases the number of cuts in the other dimension. 
        # (We track these increases with horCuts and verCuts.)

        cuts = [(-x, True) for x in horizontalCut]
        cuts.extend([(-x, False) for x in verticalCut])
        heapify(cuts)

        horizontal_cuts, vertical_cuts, ans = 1, 1, 0

        while cuts:
            cost, is_horizontal = heappop(cuts)

            if is_horizontal:
                ans -= cost * vertical_cuts
                horizontal_cuts += 1
            else:
                ans -= cost * horizontal_cuts
                vertical_cuts += 1

        return ans
            
        
# @lc code=end

