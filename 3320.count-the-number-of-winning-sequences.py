#
# @lc app=leetcode id=3320 lang=python3
#
# [3320] Count The Number of Winning Sequences
#

# @lc code=start
from collections import Counter

class Solution:
    def countWinningSequences(self, s: str) -> int:
        # dp[i][j][v] means the number of sequence,
        # that in the s + 1 round,
        # Bob get v more points,
        # and summons jth magical creatures in the last round.

        # So we enumerate the Bob's previous action j2,
        # dp[i][j][v + d] = sum(dp[i - 1][j2][v]),
        # where j != j2 and d is the delta of score.

        MOD = 10 ** 9 + 7
        n = len(s)
        s = ['FWE'.find(c) for c in s]
        dp = [[Counter() for j in range(3)] for i in range(n)]

        for i in range(n):
            for j in range(3):
                d = (j - s[i] + 1) % 3 - 1
                if i == 0:
                    dp[i][j][d] = 1
                else:
                    for j2 in range(3):
                        if j != j2:
                            for v in dp[i - 1][j2]:
                                dp[i][j][v + d] += dp[i - 1][j2][v]
                                dp[i][j][v + d] %= MOD

        res = 0
        for j in range(3):
            for v in range(1, n + 1):
                res += dp[n - 1][j][v]

        return res % MOD

        
# @lc code=end

