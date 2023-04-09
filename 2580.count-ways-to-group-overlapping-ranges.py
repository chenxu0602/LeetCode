#
# @lc app=leetcode id=2580 lang=python3
#
# [2580] Count Ways to Group Overlapping Ranges
#

# @lc code=start
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:

        """
        MOD = 10**9 + 7
        pre = -1
        res = 0
        for l, r in sorted(ranges):
            res += pre < l
            pre = max(pre, r)
        return pow(2, res, MOD)
        """

        MOD = 10 ** 9 + 7
        cnt, hi = 1, -1
        for l, r in sorted(ranges):
            if hi < l:
                cnt <<= 1
                cnt %= MOD
            hi = max(hi, r)
        return cnt

        

        
# @lc code=end

