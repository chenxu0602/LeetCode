#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (61.55%)
# Likes:    716
# Dislikes: 66
# Total Accepted:    115.8K
# Total Submissions: 189.4K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
# 
# (Here, the distance between two points on a plane is the Euclidean
# distance.)
# 
# You may return the answer in any order.  The answer is guaranteed to be
# unique (except for the order that it is in.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# 
# 
# 
#
from random import randint
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # Sort
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        # points.sort(key=lambda P: P[0]**2 + P[1]**2)
        # return points[:K]

        # Heap
        # Time  complexity: O(NlogN)
        # Space complexity: O(K)
        # heap = []
        # for x, y in points:
        #     dist = -(x**2 + y**2)
        #     if len(heap) == K:
        #         heapq.heappushpop(heap, (dist, x, y))
        #     else:
        #         heapq.heappush(heap, (dist, x, y))
        # return [(x, y) for dist, x, y in heap]

        # QuickSelect
        # Time  complexity: O(N) in average case and O(N^2) in the worst case.
        # Space complexity: O(N)
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def partition(lo, hi):
            i = lo
            pivot = dist(hi)
            for j in range(lo, hi):
                if dist(j) < pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[hi] = points[hi], points[i]
            return i

        def quickSelect(lo, hi, K):
            pi = partition(lo, hi)
            if K < pi - lo + 1:
                quickSelect(lo, pi - 1, K)
            elif K > pi - lo + 1:
                quickSelect(pi + 1, hi, K - (pi - lo + 1))

        quickSelect(0, len(points) - 1, K)
        return points[:K]







        

