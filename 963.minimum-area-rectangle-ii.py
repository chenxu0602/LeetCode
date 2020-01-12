#
# @lc app=leetcode id=963 lang=python3
#
# [963] Minimum Area Rectangle II
#
# https://leetcode.com/problems/minimum-area-rectangle-ii/description/
#
# algorithms
# Medium (46.52%)
# Likes:    80
# Dislikes: 132
# Total Accepted:    6.6K
# Total Submissions: 14.2K
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
from collections import defaultdict
from itertools import combinations

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
       points = [complex(*z) for z in points] 
       seen = defaultdict(list)

       for P, Q in combinations(points, 2):
           center = (P + Q) / 2
           radius = abs(center - P)
           seen[center, radius].append(P)

       ans = float("inf")
       for (center, radius), candidates in seen.items():
          for P, Q in combinations(candidates, 2):
             ans = min(ans, abs(P-Q) * abs(P - (2*center-Q)))

       return ans if ans < float("inf") else 0



