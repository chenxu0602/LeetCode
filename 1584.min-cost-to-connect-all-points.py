#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (49.03%)
# Likes:    295
# Dislikes: 24
# Total Accepted:    10.5K
# Total Submissions: 21.3K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].
# 
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
# absolute value of val.
# 
# Return the minimum cost to make all points connected. All points are
# connected if there is exactly one simple path between any two points.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:
# 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# 
# 
# Example 3:
# 
# 
# Input: points = [[0,0],[1,1],[1,0],[-1,1]]
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: points = [[-1000000,-1000000],[1000000,1000000]]
# Output: 4000000
# 
# 
# Example 5:
# 
# 
# Input: points = [[0,0]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.
# 
# 
#

# @lc code=start
from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's Algorithm
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        n = len(points)
        if n == 1: return 0

        res, curr = 0, 0
        dist = [float("inf")] * n
        visited = set()

        for _ in range(n - 1):
            x0, y0 = points[curr]
            visited.add(curr)

            for j, (x, y) in enumerate(points):
                if j in visited:
                    continue
                dist[j] = min(dist[j], abs(x - x0) + abs(y - y0))

            delta, curr = min((d, j) for j, d in enumerate(dist))
            dist[curr] = float("inf")
            res += delta

        return res


        # dist = defaultdict(lambda: defaultdict(int))
        # n = len(points)

        # if n <= 1: return 0
        # if n == 2:
        #     return abs(points[0][0] - points[1][0]) + abs(points[0][1] - points[1][1])

        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         dist[j][i] = dist[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        # seen, start = set(), 0
        # seen.add(start)
        # heap = []

        # for k, v in dist[start].items():
        #     heapq.heappush(heap, (v, k))

        # ans = 0
        # while heap:
        #     if len(seen) == len(points):
        #         return ans

        #     d, node = heapq.heappop(heap)
        #     if node not in seen:
        #         seen.add(node)
        #         ans += d
        #         for k, v in dist[node].items():
        #             heapq.heappush(heap, (v, k))




        
# @lc code=end

