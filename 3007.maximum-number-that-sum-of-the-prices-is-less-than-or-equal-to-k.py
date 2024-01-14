#
# @lc app=leetcode id=3007 lang=python3
#
# [3007] Maximum Number That Sum of the Prices Is Less Than or Equal to K
#

# @lc code=start
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:

        def F(m):
            count = 0
            for i in range(1, 80):
                bit = (i * x) - 1
                S = 1 << bit
                B = m // S

                count += S * (B // 2)
                if B & 1:
                    count += m % S

            return count


        l, r = 0, 10**20
        while l + 1 < r:
            m = (l + r) >> 1
            if F(m + 1) <= k: 
                l = m
            else:
                r = m

        return l
        
# @lc code=end

