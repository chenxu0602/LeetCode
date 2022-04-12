#
# @lc app=leetcode id=2223 lang=python3
#
# [2223] Sum of Scores of Built Strings
#

# @lc code=start
class Solution:
    def sumScores(self, s: str) -> int:

        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0

            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])

                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1

                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1

            return z


        return sum(z_function(s)) + len(s)
        
# @lc code=end

