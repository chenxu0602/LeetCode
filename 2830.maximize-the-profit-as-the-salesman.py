#
# @lc app=leetcode id=2830 lang=python3
#
# [2830] Maximize the Profit as the Salesman
#

# @lc code=start
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:

        # Not sell it, f[n-1] = f[n-2]
        # Sell it, f[n-1] = f[start-1] + gold
        # Time  complexity: O(n + m)  where m is the length of offers
        # Space complexity: O(n + m)
        # groups = [[] for _ in range(n)]
        # for start, end, gold in offers:
        #     groups[end] += (start, gold),

        # f = [0] * (n + 1)
        # for end, x in enumerate(groups):
        #     f[end + 1] = f[end]
        #     for start, gold in x:
        #         f[end + 1] = max(f[end + 1], f[start] + gold)

        # return f[n]


        dp = [0] * (n + 1)
        m = [[] for _ in range(n)]
        for s, e, g in offers:
            m[e] += (s, g),

        for e in range(1, n + 1):
            dp[e] = dp[e - 1]
            for s, g in m[e - 1]:
                dp[e] = max(dp[e], dp[s] + g)

        return dp[-1]
        
# @lc code=end

