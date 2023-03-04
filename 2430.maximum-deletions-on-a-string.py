#
# @lc app=leetcode id=2430 lang=python3
#
# [2430] Maximum Deletions on a String
#

# @lc code=start
class Solution:
    def deleteString(self, s: str) -> int:

        n = len(s)
        if len(set(s)) == 1: return n

        lcs = [[0] * (n + 1) for _ in range(n + 1)]
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    lcs[i][j] = lcs[i + 1][j + 1] + 1
                if lcs[i][j] >= j - i:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[0]
        
# @lc code=end

