#
# @lc app=leetcode id=2806 lang=python3
#
# [2806] Account Balance After Rounded Purchase
#

# @lc code=start
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:

        return 100 - int(int(purchaseAmount / 10 + 0.5) * 10)
        
# @lc code=end

