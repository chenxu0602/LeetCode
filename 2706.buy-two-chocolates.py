#
# @lc app=leetcode id=2706 lang=python3
#
# [2706] Buy Two Chocolates
#

# @lc code=start
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        first = second = float("inf")
        for p in prices:
            if p < first:
                first, second = p, first 
            elif p < second:
                second = p

        min_p = first + second 
        return money - min_p if min_p <= money else money 
    
        
# @lc code=end

