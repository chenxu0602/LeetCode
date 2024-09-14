#
# @lc app=leetcode id=3219 lang=python3
#
# [3219] Minimum Cost for Cutting Cake II
#

# @lc code=start
from heapq import heappush, heappop, heapify

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:

        # cuts = [(-x, True) for x in horizontalCut]
        # cuts.extend([(-x, False) for x in verticalCut])
        # heapify(cuts)

        # horizontal_cuts, vertical_cuts, ans = 1, 1, 0

        # while cuts:
        #     cost, is_horizontal = heappop(cuts)

        #     if is_horizontal:
        #         ans -= cost * vertical_cuts
        #         horizontal_cuts += 1
        #     else:
        #         ans -= cost * horizontal_cuts
        #         vertical_cuts += 1 

        # return ans

        hCuts, vCuts = [0] * 1001, [0] * 1001
        for i in horizontalCut: hCuts[i] += 1
        for j in verticalCut:   vCuts[j] += 1

        hParts, vParts, ans = 1, 1, 0
        for i in range(1000, 0, -1):
            ans += i * vParts * hCuts[i]
            hParts += hCuts[i]

            ans += i * hParts * vCuts[i]
            vParts += vCuts[i]

        return ans



# @lc code=end

