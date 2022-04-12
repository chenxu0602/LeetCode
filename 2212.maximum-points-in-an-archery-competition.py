#
# @lc app=leetcode id=2212 lang=python3
#
# [2212] Maximum Points in an Archery Competition
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:

        # Let dp(k, numArrows) is the maximum score Bob can get if we compute sections from [k...11] and numArrows arrows.
        # Time  complexity: O(2x12xnumArrows)
        # Space complexity: O(12xnumArrows)
        @lru_cache(None)
        def dp(k, numArrows):
            if k == 12 or numArrows <= 0:
                return 0

            maxScore = dp(k + 1, numArrows) # Bob Lose
            if numArrows > aliceArrows[k]:
                maxScore = max(maxScore, dp(k + 1, numArrows - aliceArrows[k] - 1) + k)
            
            return maxScore

        # backtracking
        ans = [0] * 12
        remainBobArrows = numArrows
        for k in range(12):
            if dp(k, numArrows) != dp(k + 1, numArrows): # If Bob wins
                ans[k] = aliceArrows[k] + 1
                numArrows -= ans[k]
                remainBobArrows -= ans[k]

        # In case of having remain arrows then it means in all sections Bob always win 
        # then we can distribute the remain to any section, here we simple choose first section.
        ans[0] += remainBobArrows

        return ans
        
# @lc code=end

