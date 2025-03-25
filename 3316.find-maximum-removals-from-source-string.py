#
# @lc app=leetcode id=3316 lang=python3
#
# [3316] Find Maximum Removals From Source String
#

# @lc code=start
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:

        m, n = map(len, (source, pattern))
        s = set(targetIndices)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n, -1, -1):
                if j == n:
                    dp[i][j] = int(i in s) + dp[i + 1][j]
                else:
                    dp[i][j] = int(i in s) + dp[i + 1][j]
                    if source[i] == pattern[j]:
                        dp[i][j] = max(dp[i][j], dp[i + 1][j + 1])

        return dp[0][0] if dp[0][0] != float('-inf') else 0

        
# @lc code=end

