#
# @lc app=leetcode id=256 lang=python3
#
# [256] Paint House
#
# https://leetcode.com/problems/paint-house/description/
#
# algorithms
# Easy (49.59%)
# Likes:    479
# Dislikes: 50
# Total Accepted:    64.5K
# Total Submissions: 128.3K
# Testcase Example:  '[[17,2,17],[16,16,5],[14,3,19]]'
#
# There are a row of n houses, each house can be painted with one of the three
# colors: red, blue or green. The cost of painting each house with a certain
# color is different. You have to paint all the houses such that no two
# adjacent houses have the same color.
# 
# The cost of painting each house with a certain color is represented by a n x
# 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color red; costs[1][2] is the cost of painting house 1 with color green, and
# so on... Find the minimum cost to paint all houses.
# 
# Note:
# All costs are positive integers.
# 
# Example:
# 
# 
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2
# into blue. 
# Minimum cost: 2 + 5 + 3 = 10.
# 
# 
#

# @lc code=start
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # O(n) / O(1)
        # for i in reversed(range(len(costs) - 1)):
        #     # Total cost of painting ith house red.
        #     costs[i][0] += min(costs[i+1][1], costs[i+1][2])
        #     # Total cost of painting nth house green.
        #     costs[i][1] += min(costs[i+1][0], costs[i+1][2])
        #     # Total cost of painting nth house blue.
        #     costs[i][2] += min(costs[i+1][0], costs[i+1][1])

        # if len(costs) == 0: return 0
        # return min(costs[0])


        # colors = [0] * 3
        # for cost in costs:
        #     colors = [cost[i] + min(colors[:i] + colors[i+1:]) for i in range(3)]
        # return min(colors)

        
        red, blue, green = 0, 0, 0
        for cr, cb, cg in costs:
            red, blue, green = min(blue, green) + cr, min(red, green) + cb, min(red, blue) + cg
        return min(red, blue, green)
# @lc code=end

