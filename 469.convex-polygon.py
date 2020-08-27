#
# @lc app=leetcode id=469 lang=python3
#
# [469] Convex Polygon
#
# https://leetcode.com/problems/convex-polygon/description/
#
# algorithms
# Medium (35.60%)
# Likes:    57
# Dislikes: 159
# Total Accepted:    7.1K
# Total Submissions: 20.1K
# Testcase Example:  '[[0,0],[0,1],[1,1],[1,0]]'
#
# Given a list of points that form a polygon when joined sequentially, find if
# this polygon is convex (Convex polygon definition).
# 
# 
# 
# Note:
# 
# 
# There are at least 3 and at most 10,000 points.
# Coordinates are in the range -10,000 to 10,000.
# You may assume the polygon formed by given points is always a simple polygon
# (Simple polygon definition). In other words, we ensure that exactly two edges
# intersect at each vertex, and that edges otherwise don't intersect each
# other.
# 
# 
# 
# 
# Example 1:
# 
# 
# [[0,0],[0,1],[1,1],[1,0]]
# 
# Answer: True
# 
# Explanation:
# 
# 
# Example 2:
# 
# 
# [[0,0],[0,10],[10,10],[10,0],[5,5]]
# 
# Answer: False
# 
# Explanation:
# 
# 
#
class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:

        # right-hand rule, only z-axis needs to be considered
        def direction(a, b, c):
            return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

        d = None
        for i in range(0, len(points)):
            a = direction(points[i-2], points[i-1], points[i])
            if a == 0:
                continue
            if d is None:
                d = a
            else:
                if a * d < 0:
                    return False

        if direction(points[-2], points[-1], points[0]) * d < 0:
            return False

        return True


