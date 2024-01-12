#
# @lc app=leetcode id=2999 lang=python3
#
# [2999] Count the Number of Powerful Integers
#

# @lc code=start
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def at_most(x):
            str_x = str(x)
            ans = 0
            for i in range(len(str_x) - len(s)):
                ans += min(limit + 1, int(str_x[i])) * (limit + 1) ** (len(str_x) - len(s) - i - 1)
                if int(str_x[i]) > limit:
                    break
            else:
                ans += (int(str_x[-len(s):]) >= int(s))

            return ans

        return at_most(finish) - at_most(start - 1)
        
# @lc code=end

