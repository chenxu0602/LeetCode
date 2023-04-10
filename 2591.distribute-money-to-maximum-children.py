#
# @lc app=leetcode id=2591 lang=python3
#
# [2591] Distribute Money to Maximum Children
#

# @lc code=start
class Solution:
    def distMoney(self, money: int, children: int) -> int:

        if money < children: return -1
        n = 8 * children - money

        if n <= 0:
            return children - (n < 0)

        ans, rem = divmod(money - children, 7)
        return ans - ((ans, rem) == (children - 1, 3))
        
# @lc code=end

