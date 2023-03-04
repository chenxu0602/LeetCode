#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        G, ans = math.gcd(a, b), 0

        for x in range(1, 1000):
            if not G % x:
                ans += 1

                if G == x:
                    return ans

        return ans + 1
        
# @lc code=end

