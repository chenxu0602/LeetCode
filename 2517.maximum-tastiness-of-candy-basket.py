#
# @lc app=leetcode id=2517 lang=python3
#
# [2517] Maximum Tastiness of Candy Basket
#

# @lc code=start
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:

        price.sort()
        def check(x):
            last, count, i = price[0], 1, 1
            while count < k and i < len(price):
                if price[i] - last >= x:
                    last, count = price[i], count + 1
                i += 1
            return count == k

        lo, hi = 0, 10**9
        while lo < hi:
            mi = (lo + hi) // 2
            if check(mi): lo = mi + 1
            else: hi = mi
        return lo - 1
        
# @lc code=end

