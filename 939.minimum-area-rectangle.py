#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#
# https://leetcode.com/problems/minimum-area-rectangle/description/
#
# algorithms
# Medium (51.13%)
# Likes:    350
# Dislikes: 68
# Total Accepted:    25.5K
# Total Submissions: 49.7K
# Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
#
# Given a set of points in the xy-plane, determine the minimum area of a
# rectangle formed from these points, with sides parallel to the x and y axes.
# 
# If there isn't any rectangle, return 0.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
# 
# 
# 
#
from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)

        lastx = {}
        ans = float("inf")

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float("inf") else 0


        

