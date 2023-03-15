#
# @lc app=leetcode id=2484 lang=python3
#
# [2484] Count Palindromic Subsequences
#

# @lc code=start
class Solution:
    def countPalindromes(self, s: str) -> int:

        ans = 0
        MOD = 10**9 + 7

        for x in range(10):
            for y in range(10):
                pattern = f"{x}{y}|{y}{x}"
                dp = [0] * 6
                dp[-1] = 1
                for i in range(len(s)):
                    for j in range(5):
                        if s[i] == pattern[j] or j == 2: # j == 2 is the middle
                            dp[j] += dp[j + 1]

                ans = (ans + dp[0]) % MOD

        return ans

        
# @lc code=end

