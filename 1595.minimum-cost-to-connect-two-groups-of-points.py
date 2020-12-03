#
# @lc app=leetcode id=1595 lang=python3
#
# [1595] Minimum Cost to Connect Two Groups of Points
#
# https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/description/
#
# algorithms
# Hard (41.94%)
# Likes:    162
# Dislikes: 7
# Total Accepted:    3.5K
# Total Submissions: 8.3K
# Testcase Example:  '[[15,96],[36,2]]'
#
# You are given two groups of points where the first group has size1 points,
# the second group has size2 points, and size1 >= size2.
# 
# The cost of the connection between any two points are given in an size1 x
# size2 matrix where cost[i][j] is the cost of connecting point i of the first
# group and point j of the second group. The groups are connected if each point
# in both groups is connected to one or more points in the opposite group. In
# other words, each point in the first group must be connected to at least one
# point in the second group, and each point in the second group must be
# connected to at least one point in the first group.
# 
# Return the minimum cost it takes to connect the two groups.
# 
# 
# Example 1:
# 
# 
# Input: cost = [[15, 96], [36, 2]]
# Output: 17
# Explanation: The optimal way of connecting the groups is:
# 1--A
# 2--B
# This results in a total cost of 17.
# 
# 
# Example 2:
# 
# 
# Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
# Output: 4
# Explanation: The optimal way of connecting the groups is:
# 1--A
# 2--B
# 2--C
# 3--A
# This results in a total cost of 4.
# Note that there are multiple points connected to point 2 in the first group
# and point A in the second group. This does not matter as there is no limit to
# the number of points that can be connected. We only care about the minimum
# total cost.
# 
# 
# Example 3:
# 
# 
# Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
# Output: 10
# 
# 
# 
# Constraints:
# 
# 
# size1 == cost.length
# size2 == cost[i].length
# 1 <= size1, size2 <= 12
# size1 >= size2
# 0 <= cost[i][j] <= 100
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        # 1. Connect all group1 nodes to group2. Each group1 node only sends out 1 edge.
        # 2. For all the unconnected nodes in group2, connect them with their min-cost counterparty in group1.
        m, n = map(len, (cost, cost[0]))
        min_arr = [min(x) for x in zip(*cost)]

        @lru_cache(None)
        def dp(i, mask):
            if i == m:
                return sum((min_arr[j] for j in range(n) if mask & 1 << j == 0) or [0])

            ans = float("inf")
            for j in range(n):
                ans = min(ans, cost[i][j] + dp(i + 1, mask | 1 << j))

            return ans


        return dp(0, 0)
        
# @lc code=end

