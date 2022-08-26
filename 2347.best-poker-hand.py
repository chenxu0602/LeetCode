#
# @lc app=leetcode id=2347 lang=python3
#
# [2347] Best Poker Hand
#

# @lc code=start
from collections import Counter

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        if max(suits) == min(suits):
            return "Flush"

        match max(Counter(ranks).values()):
            case 5 | 4 | 3:
                return "Three of a Kind"
            case 2:
                return "Pair"
            case _:
                return "High Card"


        
# @lc code=end

