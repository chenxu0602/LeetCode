#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/
#
# algorithms
# Easy (67.77%)
# Likes:    25
# Dislikes: 5
# Total Accepted:    6.1K
# Total Submissions: 9K
# Testcase Example:  '3\n4\n[[1,2],[3,1],[2,4],[2,3],[4,4]]'
#
# You are given two integers, x and y, which represent your current location on
# a Cartesian grid: (x, y). You are also given an array points where each
# points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is
# valid if it shares the same x-coordinate or the same y-coordinate as your
# location.
# 
# Return the index (0-indexed) of the valid point with the smallest Manhattan
# distance from your current location. If there are multiple, return the valid
# point with the smallest index. If there are no valid points, return -1.
# 
# The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 -
# x2) + abs(y1 - y2).
# 
# 
# Example 1:
# 
# 
# Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# Output: 2
# Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the
# valid points, [2,4] and [4,4] have the smallest Manhattan distance from your
# current location, with a distance of 1. [2,4] has the smallest index, so
# return 2.
# 
# Example 2:
# 
# 
# Input: x = 3, y = 4, points = [[3,4]]
# Output: 0
# Explanation: The answer is allowed to be on the same location as your current
# location.
# 
# Example 3:
# 
# 
# Input: x = 3, y = 4, points = [[2,3]]
# Output: -1
# Explanation: There are no valid points.
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 10^4
# points[i].length == 2
# 1 <= x, y, ai, bi <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        return min([(i, z[0], z[1]) for i, z in enumerate(points) if (z[0] == x or z[1] == y)] or [(-1, 0, 0)], \
            key=lambda z: abs(z[1] - x) + abs(z[2] - y))[0]
        
# @lc code=end

