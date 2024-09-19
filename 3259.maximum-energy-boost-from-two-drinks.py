#
# @lc app=leetcode id=3259 lang=python3
#
# [3259] Maximum Energy Boost From Two Drinks
#

# @lc code=start
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:

        n = len(energyDrinkA)

        dpA, dpB = [0] * n, [0] * n
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]

        for i in range(1, n):
            dpA[i] = max(dpA[i - 1] + energyDrinkA[i], dpB[i - 1])
            dpB[i] = max(dpB[i - 1] + energyDrinkB[i], dpA[i - 1])

        max_ = max(dpA[-1], dpB[-1])
        return max_
        
# @lc code=end

