#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:

        cur = set()
        res = 1

        for c in s:
            if c in cur:
                cur = set()
                res += 1
            cur.add(c)

        return res
        
# @lc code=end

