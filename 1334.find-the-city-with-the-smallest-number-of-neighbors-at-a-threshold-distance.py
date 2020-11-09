#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
#
# algorithms
# Medium (45.84%)
# Likes:    388
# Dislikes: 27
# Total Accepted:    15.8K
# Total Submissions: 34.5K
# Testcase Example:  '4\n[[0,1,3],[1,2,1],[1,3,4],[2,3,1]]\n4'
#
# There are n cities numbered from 0 to n-1. Given the array edges where
# edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge
# between cities fromi and toi, and given the integer distanceThreshold.
# 
# Return the city with the smallest number of cities that are reachable through
# some path and whose distance is at most distanceThreshold, If there are
# multiple such cities, return the city with the greatest number.
# 
# Notice that the distance of a path connecting cities i and j is equal to the
# sum of the edges' weights along that path.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold =
# 4
# Output: 3
# Explanation: The figure above describes the graph. 
# The neighboring cities at a distanceThreshold = 4 for each city are:
# City 0 -> [City 1, City 2] 
# City 1 -> [City 0, City 2, City 3] 
# City 2 -> [City 0, City 1, City 3] 
# City 3 -> [City 1, City 2] 
# Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we
# have to return city 3 since it has the greatest number.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],
# distanceThreshold = 2
# Output: 0
# Explanation: The figure above describes the graph. 
# The neighboring cities at a distanceThreshold = 2 for each city are:
# City 0 -> [City 1] 
# City 1 -> [City 0, City 4] 
# City 2 -> [City 3, City 4] 
# City 3 -> [City 2, City 4]
# City 4 -> [City 1, City 2, City 3] 
# The city 0 has 1 neighboring city at a distanceThreshold = 2.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 100
# 1 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti, distanceThreshold <= 10^4
# All pairs (fromi, toi) are distinct.
# 
# 
#

# @lc code=start
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Floyd–Warshall algorithm
        # Time  complexity: O(N^3)
        # Space complexity: O(N^2)
        dist = [[float("inf")] * n for _ in range(n)]
        for i, j, w in edges:
            dist[i][j] = dist[j][i] = w

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 

        res = {sum(d <= distanceThreshold for d in dist[i]): i for i in range(n)}
        return res[min(res)]
        
# @lc code=end

