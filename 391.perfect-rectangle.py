#
# @lc app=leetcode id=391 lang=python3
#
# [391] Perfect Rectangle
#
# https://leetcode.com/problems/perfect-rectangle/description/
#
# algorithms
# Hard (28.22%)
# Likes:    234
# Dislikes: 49
# Total Accepted:    18.6K
# Total Submissions: 65.7K
# Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
#
# Given N axis-aligned rectangles where N > 0, determine if they all together
# form an exact cover of a rectangular region.
# 
# Each rectangle is represented as a bottom-left point and a top-right point.
# For example, a unit square is represented as [1,1,2,2]. (coordinate of
# bottom-left point is (1, 1) and top-right point is (2, 2)).
# 
# 
# 
# Example 1:
# 
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4],
# ⁠ [1,3,2,4],
# ⁠ [2,3,3,4]
# ]
# 
# Return true. All 5 rectangles together form an exact cover of a rectangular
# region.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# rectangles = [
# ⁠ [1,1,2,3],
# ⁠ [1,3,2,4],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4]
# ]
# 
# Return false. Because there is a gap between the two rectangular
# regions.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [3,2,4,4]
# ]
# 
# Return false. Because there is a gap in the top center.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 4:
# 
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [2,2,4,4]
# ]
# 
# Return false. Because two of the rectangles overlap with each other.
# 
# 
# 
#
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, corners = 0, set()
        a, c = lambda: (X - x) * (Y - y), lambda: {(x, y), (x, Y), (X, y), (X, Y)}
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= c()

        x, y, X, Y = (f(z) for f, z in zip((min, min, max, max), zip(*rectangles)))
        return area == a() and corners == c()

        
        

