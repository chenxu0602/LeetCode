#
# @lc app=leetcode id=3207 lang=python3
#
# [3207] Maximum Points After Enemy Battles
#

# @lc code=start
class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:

        enemyEnergies.sort()
        tot = 0
        i, j = 0, len(enemyEnergies) - 1

        while i <= j:
            if currentEnergy >= enemyEnergies[i]:
                tot += currentEnergy // enemyEnergies[i]
                currentEnergy = currentEnergy % enemyEnergies[i]
            else:
                currentEnergy += enemyEnergies[j]
                j -= 1
            
            if tot == 0:
                break

        return tot
        

        
# @lc code=end

