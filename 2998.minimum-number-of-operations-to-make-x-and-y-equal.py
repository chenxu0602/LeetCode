#
# @lc app=leetcode id=2998 lang=python3
#
# [2998] Minimum Number of Operations to Make X and Y Equal
#

# @lc code=start
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:

        # When x > y, we have 4 options.
        # plus then divide 5
        # minus then divide 5
        # plus then divide 11
        # minus then divide 11

        if x <= y: return y - x
        res = x - y
        for v in [5, 11]:
            res = min(res, self.minimumOperationsToMakeEqual(x // v, y) + 1 + x % v)
            res = min(res, self.minimumOperationsToMakeEqual(x // v + 1, y) + 1 + v - x % v)

        return res

        
# @lc code=end

