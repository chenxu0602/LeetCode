#
# @lc app=leetcode id=2222 lang=python3
#
# [2222] Number of Ways to Select Buildings
#

# @lc code=start
class Solution:
    def numberOfWays(self, s: str) -> int:
        a = b = ans = 0
        for i in range(len(s)):
            if s[i] == '1':
                a += 1
            else:
                b += 1

        c = d = 0
        for i in range(len(s)):
            if s[i] == '1':
                ans += (d * b)
                a -= 1
                c += 1
            else:
                ans += (a * c)
                b -= 1
                d += 1

        return ans

        
# @lc code=end

