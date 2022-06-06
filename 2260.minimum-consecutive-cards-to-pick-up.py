#
# @lc app=leetcode id=2260 lang=python3
#
# [2260] Minimum Consecutive Cards to Pick Up
#

# @lc code=start
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        min_pick = float("inf")
        seen = {}
        for i, v in enumerate(cards):
            if v in seen:
                if i - seen[v] + 1 < min_pick:
                    min_pick = i - seen[v] + 1
            seen[v] = i

        if min_pick == float("inf"):
            return -1

        return min_pick
        
# @lc code=end

