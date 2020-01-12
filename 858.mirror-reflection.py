#
# @lc app=leetcode id=858 lang=python3
#
# [858] Mirror Reflection
#
# https://leetcode.com/problems/mirror-reflection/description/
#
# algorithms
# Medium (52.13%)
# Likes:    145
# Dislikes: 237
# Total Accepted:    7.3K
# Total Submissions: 14K
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
from fractions import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        p = (p / g) % 2
        q = (q / g) % 2

        return 1 if p and q else 0 if p else 2
        

