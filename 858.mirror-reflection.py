#
# @lc app=leetcode id=858 lang=python3
#
# [858] Mirror Reflection
#
# https://leetcode.com/problems/mirror-reflection/description/
#
# algorithms
# Medium (53.61%)
# Likes:    197
# Dislikes: 306
# Total Accepted:    9.9K
# Total Submissions: 18.2K
# Testcase Example:  '2\n1'
#
# There is a special square room with mirrors on each of the four walls.
# Except for the southwest corner, there are receptors on each of the remaining
# corners, numbered 0, 1, and 2.
# 
# The square room has walls of length p, and a laser ray from the southwest
# corner first meets the east wall at a distance q from the 0th receptor.
# 
# Return the number of the receptor that the ray meets first.  (It is
# guaranteed that the ray will meet a receptor eventually.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back
# to the left wall.
# 
# 
# 
# Note:
# 
# 
# 1 <= p <= 1000
# 0 <= q <= p
# 
# 
# 
#

# @lc code=start
from fractions import Fraction

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Time  complexity: O(P)
        # Space complexity: O(1)
        x = y = 0
        rx, ry = p, q
        targets = [(p, 0), (p, p), (0, p)]

        while (x, y) not in targets:
            # Want smallest t so that some x + rx, y + ry is 0 or p
            # x + rxt = 0, then t = -x/rx etc.
            t = float("inf")
            for v in [Fraction(-x, rx), Fraction(-y, ry), Fraction(p - x, rx), Fraction(p - y, ry)]:
                if v > 0: t = min(t, v)

            x += rx * t
            y += ry * t

            # update rx, ry
            if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
                rx *= -1
            if y == p or y == 0:
                ry *= -1

        return 1 if x == y == p else 0 if x == p else 2
        
# @lc code=end

