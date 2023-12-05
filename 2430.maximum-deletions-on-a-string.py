#
# @lc app=leetcode id=2430 lang=python3
#
# [2430] Maximum Deletions on a String
#

# @lc code=start
class Solution:
    def deleteString(self, s: str) -> int:

        # lcs[i][j] means the length of the longest common substring.
        # If lcs[i][j] = k,
        # then s.substring(i, i + k) == s.substring(j, j + k)
        # and s.substring(i, i + k + 1) != s.substring(j, j + k + 1).
        # This can be done in O(n^2).

        # dp[i] mean the the maximum number of operations to delete
        # the substring starting at s[i].

        # If lcs[i][j] >= j - i,
        # s.substring(i, j) == s.substring(j, j + j - i)
        # this means we can delete the prefix s.substring(i, j) from s.substring(i),
        # and it changes to s.substring(j).
        # And we update dp[i] = max(dp[i], dp[j] + 1)

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

