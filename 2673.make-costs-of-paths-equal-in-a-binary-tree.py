#
# @lc app=leetcode id=2673 lang=python3
#
# [2673] Make Costs of Paths Equal in a Binary Tree
#

# @lc code=start
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:

        """
        self.res = 0
        def dfs(i):
            if i >= len(cost): return 0
            a, b = dfs(2 * i + 1), dfs(2 * i + 2)
            self.res += abs(a - b)
            return cost[i] + max(a, b)
        
        dfs(0)
        return self.res
        """

        res = 0
        for i in range(n // 2 - 1, -1, -1):
            l, r = 2 * i + 1, i * 2 + 2
            res += abs(cost[l] - cost[r])
            cost[i] += max(cost[l], cost[r])

        return res
        
# @lc code=end

