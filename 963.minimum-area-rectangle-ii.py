#
# @lc app=leetcode id=963 lang=python3
#
# [963] Minimum Area Rectangle II
#
# https://leetcode.com/problems/minimum-area-rectangle-ii/description/
#
# algorithms
# Medium (48.63%)
# Likes:    110
# Dislikes: 176
# Total Accepted:    9K
# Total Submissions: 18.5K
# Testcase Example:  '[[1,2],[2,1],[1,0],[0,1]]'
#
# Given a set of points in the xy-plane, determine the minimum area of any
# rectangle formed from these points, with sides not necessarily parallel to
# the x and y axes.
# 
# If there isn't any rectangle, return 0.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[1,2],[2,1],[1,0],[0,1]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1],
# with an area of 2.
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
# Output: 1.00000
# Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0],
# with an area of 1.
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
# Output: 0
# Explanation: There is no possible rectangle to form from these points.
# 
# 
# 
# Example 4:
# 
# 
# 
# 
# Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1],
# with an area of 2.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= points.length <= 50
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
# Answers within 10^-5 of the actual value will be accepted as correct.
# 
# 
#

# @lc code=start
from collections import defaultdict
import itertools

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # Iterate Triangles
        # Say the first 3 points are p1, p2, p3, and that p2 and p3 are opposite corners of the final rectangle. The 4th point must be p4 = p2 + p3 - p1 (using vector notation) because p1, p2, p4, p3 must form a parallelogram, and p1 + (p2 - p1) + (p3 - p1) = p4.
        # Time  complexity: O(N^3)
        # Space complexity: O(N)
        # EPS = 1e-7
        # points = set(map(tuple, points))

        # ans = float("inf")
        # for p1, p2, p3 in itertools.permutations(points, 3):
        #     p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
        #     if p4 in points:
        #         v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
        #         v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
        #         if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
        #             area = abs(v21) * abs(v31)
        #             if area < ans:
        #                 ans = area
        
        # return ans if ans < float("inf") else 0


        # Iterate Centers
        # Consider opposite points AC and BD of a rectangle ABCD. They both have the same center O, which is the midpoint of AC and the midpoint of AB; and they both have the same radius dist(O, A) == dist(O, B) == dist(O, C) == dist(O, D). Notice that a necessary and sufficient condition to form a rectangle with two opposite pairs of points is that the points must have the same center and radius.
        # For each pair of points, classify them by center and radius. We only need to record one of the points P, since the other point is P' = 2 * center - P (using vector notation).
        # For each center and radius, look at every possible rectangle (two pairs of points P, P', Q, Q'). The area of this rectangle dist(P, Q) * dist(P, Q') is a candidate answer.
        # Time  complexity: O(N^2 x logN). It can be shown that the number pairs of points with the same classification is bounded by logN.
        # Space complexity: O(N)
        points = [complex(*z) for z in points]
        seen = defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        ans = float("inf")
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                ans = min(ans, abs(P - Q) * abs(P - (2 * center - Q)))

        return ans if ans < float("inf") else 0


        # O(N^3)
        # points = [complex(*z) for z in sorted(points)]
        # seen = defaultdict(list)
        # for P, Q in itertools.combinations(points, 2):
        #     seen[P - Q].append((P + Q) / 2)
        #     # Q-P, it is a vector that stores both the direction and the length of the edge
        #     # (P+Q)/2 is the mid point of the edge 
        #     # save the midpoints as a list for all edges with the same direction and length 

        # ans = float("inf")
        # for A, candidates in seen.items():
        #     for P, Q in itertools.combinations(candidates, 2):
        #         if A.real * (P - Q).real == -A.imag * (P - Q).imag:
        #             ans = min(ans, abs(A) * abs(P - Q))

        # return ans if ans < float("inf") else 0


        
# @lc code=end

