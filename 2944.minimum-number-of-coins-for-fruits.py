#
# @lc app=leetcode id=2944 lang=python3
#
# [2944] Minimum Number of Coins for Fruits
#

# @lc code=start
from functools import cache
from collections import deque

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:



        """
        # O(n^2)

        n = len(prices)

        @cache
        def dfs(i):
            if i >= n: return 0
            res = float('inf')
            for j in range(i + 1, i + i + 2 + 1):
                res = min(res, dfs(j))
            return res + prices[i]

        return dfs(0)
        """


        """
        # O(n)

        n = len(prices)
        dp = [0] * (n + 1)
        queue = deque()

        for i in range(n):
            while queue and (queue[0] + 1) * 2 < i + 1:
                queue.popleft()

            while queue and dp[queue[-1]] + prices[queue[-1]] >= dp[i] + prices[i]:
                queue.pop()

            queue += i,
            dp[i + 1] = dp[queue[0]] + prices[queue[0]]

        return dp[-1]
        """


        queue, cost = deque(), 0
        for i, price in enumerate(prices):
            while queue and queue[0][1] < i:
                queue.popleft()
            cost += price
            while queue and queue[-1][0] > cost:
                queue.pop()
            queue += (cost, 2 * i + 1),
            cost = min(cost, queue[0][0])

        return cost
        
# @lc code=end

