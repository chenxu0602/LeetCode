#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#

# @lc code=start
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        n = len(s)
        dp = [n] * (n + 1)
        for i in range(1, n + 1):
            for word in dictionary:
                if i >= len(word) and s[i - len(word):i] == word:
                    dp[i] = min(dp[i], dp[i - len(word)] - len(word))

            dp[i] = min(dp[i], dp[i - 1])
        return dp[n]
    
        
# @lc code=end

