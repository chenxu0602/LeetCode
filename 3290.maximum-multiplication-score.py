#
# @lc app=leetcode id=3290 lang=python3
#
# [3290] Maximum Multiplication Score
#

# @lc code=start
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:

        dp0 = dp1 = dp2 = dp3 = float('-inf')
        a0, a1, a2, a3 = a

        for b_elem in b:
            dp3 = max(dp3, dp2 + a3 * b_elem)
            dp2 = max(dp2, dp1 + a2 * b_elem)
            dp1 = max(dp1, dp0 + a1 * b_elem)
            dp0 = max(dp0,       a0 * b_elem)

        return dp3
        
# @lc code=end

