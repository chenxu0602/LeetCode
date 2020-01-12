#
# @lc app=leetcode id=1037 lang=python3
#
# [1037] Valid Boomerang
#
# https://leetcode.com/problems/valid-boomerang/description/
#
# algorithms
# Easy (37.65%)
# Likes:    50
# Dislikes: 157
# Total Accepted:    10.5K
# Total Submissions: 28.2K
# Testcase Example:  '[[1,1],[2,3],[3,2]]'
#
# A boomerang is a set of 3 points that are all distinct and not in a straight
# line.
# 
# Given a list of three points in the plane, return whether these points are a
# boomerang.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],[2,3],[3,2]]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[2,2],[3,3]]
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# points.length == 3
# points[i].length == 2
# 0 <= points[i][j] <= 100
# 
# 
# 
# 
# 
#
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p = points
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1]) 

