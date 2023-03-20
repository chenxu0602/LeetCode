#
# @lc app=leetcode id=2498 lang=python3
#
# [2498] Frog Jump II
#

# @lc code=start
class Solution:
    def maxJump(self, stones: List[int]) -> int:

        res= stones[1] - stones[0]
        for i in range(2, len(stones)):
            res = max(res, stones[i] - stones[i - 2])

        return res
        
# @lc code=end

