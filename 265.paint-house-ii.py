#
# @lc app=leetcode id=265 lang=python3
#
# [265] Paint House II
#
# https://leetcode.com/problems/paint-house-ii/description/
#
# algorithms
# Hard (43.66%)
# Likes:    438
# Dislikes: 17
# Total Accepted:    54.7K
# Total Submissions: 125.3K
# Testcase Example:  '[[1,5,3],[2,9,4]]'
#
# There are a row of n houses, each house can be painted with one of the k
# colors. The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the
# same color.
# 
# The cost of painting each house with a certain color is represented by a n x
# k cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color 0; costs[1][2] is the cost of painting house 1 with color 2, and so
# on... Find the minimum cost to paint all houses.
# 
# Note:
# All costs are positive integers.
# 
# Example:
# 
# 
# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum
# cost: 1 + 4 = 5; 
# Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 +
# 2 = 5. 
# 
# 
# Follow up:
# Could you solve it in O(nk) runtime?
# 
#

# @lc code=start
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        k = len(costs[0]) if costs else 0
        colors = [0] * k

        for cost in costs:
            colors = [cost[i] + min(colors[:i] + colors[i+1:], default=0) for i in range(k)]
        return min(colors) if colors else 0

        
# @lc code=end

