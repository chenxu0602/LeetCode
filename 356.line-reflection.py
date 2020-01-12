#
# @lc app=leetcode id=356 lang=python3
#
# [356] Line Reflection
#
# https://leetcode.com/problems/line-reflection/description/
#
# algorithms
# Medium (30.93%)
# Likes:    96
# Dislikes: 235
# Total Accepted:    18.7K
# Total Submissions: 60.4K
# Testcase Example:  '[[1,1],[-1,1]]'
#
# Given n points on a 2D plane, find if there is such a line parallel to y-axis
# that reflect the given points.
# 
# Example 1:
# 
# 
# Input: [[1,1],[-1,1]]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[-1,-1]]
# Output: false
# 
# 
# Follow up:
# Could you do better than O(n^2) ?
#
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = sorted(set(map(tuple, points)))
        return points == sorted((points[0][0] + points[-1][0] - x, y) for x, y in points)
        

