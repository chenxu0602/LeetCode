#
# @lc app=leetcode id=2370 lang=python3
#
# [2370] Longest Ideal Subsequence
#

# @lc code=start
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        """
        dp = [0] * 26
        for c in s:
            cur = ord(c) - ord('a')
            for i in range(max(0, cur - k), min(25, cur + k) + 1):
                dp[cur] = max(dp[i], dp[cur])
            dp[cur] += 1
        return max(dp)
        """

        dp = [0] * 128
        for c in s:
            cur = ord(c)
            dp[cur] = max(dp[cur - k:cur + k + 1]) + 1
        return max(dp)
        
# @lc code=end

