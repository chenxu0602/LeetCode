#
# @lc app=leetcode id=3253 lang=python3
#
# [3253] Construct String with Minimum Cost (Easy)
#

# @lc code=start
from functools import lru_cache

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:

        # @lru_cache(None)
        # def dp(s: str, res = float('inf')):
        #     if s == '': return 0
        #     for word, cost in zip(words, costs):
        #         if s.startswith(word):
        #             res = min(res, cost + dp(s[len(word):]))

        #     return res

        # ans = dp(target)
        # return -1 if ans == float('inf') else ans


        n = len(target)
        dp = [0] + [float('inf')] * n
        for i in range(n):
            for w, c in zip(words, costs):
                if w == target[i:i + len(w)]:
                    dp[i + len(w)] = min(dp[i + len(w)], dp[i] + c)

        return dp[-1] if dp[-1] != float('inf') else -1

        
# @lc code=end

