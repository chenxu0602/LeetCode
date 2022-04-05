#
# @lc app=leetcode id=2147 lang=python3
#
# [2147] Number of Ways to Divide a Long Corridor
#

# @lc code=start
class Solution:
    def numberOfWays(self, corridor: str) -> int:

        a = [i for i, c in enumerate(corridor) if c == 'S']
        res = 1
        for i in range(1, len(a) - 1, 2):
            res *= a[i + 1] - a[i]
        return res % (10**9 + 7) * (len(a) % 2 == 0 and len(a) >= 2)

        # a, b, c = 1, 0, 0
        # for ch in corridor:
        #     if ch == 'S':
        #         a, b, c = 0, a + c, b
        #     else:
        #         a, b, c = a + c, b, c
        # return c % (10**9 + 7)
        
# @lc code=end

