#
# @lc app=leetcode id=2719 lang=python3
#
# [2719] Count of Integers
#

# @lc code=start
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:

        def digitDP(s, min_sum, max_sum):
            n = len(s)
            dp = [[[0] * (max_sum + 10) for _ in range(2)] for _ in range(n + 1)]
            dp[n][0][0] = 1
            dp[n][1][0] = 1

            for i in range(n - 1, -1, -1):
                for tight in range(2):
                    for sm in range(max_sum + 1):
                        if tight:
                            up = int(s[i])
                            for digit in range(up + 1):
                                dp[i][1][sm] += dp[i + 1][int(digit == up)][sm - digit]
                                dp[i][1][sm] %= MOD
                        else:
                            up = 9
                            for digit in range(up + 1):
                                dp[i][0][sm] += dp[i + 1][0][sm - digit] # Don't need to worry about negative sm - digit because the last 10 elements are not used.
                                dp[i][0][sm] %= MOD

            res = 0
            for i in range(min_sum, max_sum + 1):
                res += dp[0][1][i]
                res %= MOD

            return res % MOD


        MOD = 10**9 + 7
        res = digitDP(num2, min_sum, max_sum)
        res -= digitDP(str(int(num1) - 1), min_sum, max_sum)
        return res % MOD

        
# @lc code=end

