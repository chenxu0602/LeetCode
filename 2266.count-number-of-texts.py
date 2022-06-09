#
# @lc app=leetcode id=2266 lang=python3
#
# [2266] Count Number of Texts
#

# @lc code=start
class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        dp = [1] + [0] * 4
        for i, c in enumerate(pressedKeys, 1):
            dp[i % 5] = dp[(i - 1) % 5]
            for j in range(i - 2, max(-1, i - 4 - (c in '79')), -1):
                if c == pressedKeys[j]:
                    dp[i % 5] += dp[j % 5]
                else:
                    break

            dp[i % 5] %= 10**9 + 7

        return dp[len(pressedKeys) % 5]
        
# @lc code=end

