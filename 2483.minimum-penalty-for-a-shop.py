#
# @lc app=leetcode id=2483 lang=python3
#
# [2483] Minimum Penalty for a Shop
#

# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:

        h = m = s = 0
        for i, c in enumerate(customers):
            s += (c == 'Y') * 2 - 1
            if s > m:
                m, h = s, i + 1

        return h
        
# @lc code=end

