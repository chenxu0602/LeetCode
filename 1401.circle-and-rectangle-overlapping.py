#
# @lc app=leetcode id=1401 lang=python3
#
# [1401] Circle and Rectangle Overlapping
#
# https://leetcode.com/problems/circle-and-rectangle-overlapping/description/
#
# algorithms
# Medium (42.23%)
# Likes:    131
# Dislikes: 43
# Total Accepted:    6.4K
# Total Submissions: 15.1K
# Testcase Example:  '1\n0\n0\n1\n-1\n3\n1'
#
# Given a circle represented as (radius, x_center, y_center) and an
# axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are
# the coordinates of the bottom-left corner, and (x2, y2) are the coordinates
# of the top-right corner of the rectangle.
# 
# Return True if the circle and rectangle are overlapped otherwise return
# False.
# 
# In other words, check if there are any point (xi, yi) such that belongs to
# the circle and the rectangle at the same time.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 =
# 1
# Output: true
# Explanation: Circle and rectangle share the point (1,0) 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 =
# 1
# Output: true
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 =
# 3
# Output: true
# 
# 
# Example 4:
# 
# 
# Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 =
# -1
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= radius <= 2000
# -10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
# x1 < x2
# y1 < y2
# 
# 
#

# @lc code=start
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Move the center of the circle to the coordinate origin (0, 0), then this problem becomes "is there a point (x, y) (x1 <= x <= x2, y1 <= y <= y2) satisfying x^2 + y^2 <= r^2".
        x1 -= x_center
        x2 -= x_center
        y1 -= y_center
        y2 -= y_center

        minX = min(x1 * x1, x2 * x2) if x1 * x2 > 0 else 0
        minY = min(y1 * y1, y2 * y2) if y1 * y2 > 0 else 0

        return minX + minY <= radius ** 2
        
# @lc code=end

