#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#
# https://leetcode.com/problems/robot-bounded-in-circle/description/
#
# algorithms
# Medium (44.70%)
# Likes:    129
# Dislikes: 83
# Total Accepted:    8.9K
# Total Submissions: 19.5K
# Testcase Example:  '"GGLLGG"'
#
# On an infinite plane, a robot initially stands at (0, 0) and faces north.
# The robot can receive one of three instructions:
# 
# 
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# 
# 
# The robot performs the instructions given in order, and repeats them
# forever.
# 
# Return true if and only if there exists a circle in the plane such that the
# robot never leaves the circle.
# 
# 
# 
# Example 1:
# 
# 
# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to
# (0,0).
# When repeating these instructions, the robot remains in the circle of radius
# 2 centered at the origin.
# 
# 
# Example 2:
# 
# 
# Input: "GG"
# Output: false
# Explanation: 
# The robot moves north indefinitely.
# 
# 
# Example 3:
# 
# 
# Input: "GL"
# Output: true
# Explanation: 
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) ->
# ...
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= instructions.length <= 100
# instructions[i] is in {'G', 'L', 'R'}
# 
# 
#
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        # x, y, dx, dy = 0, 0, 0, 1
        # for i in instructions:
        #     if i == 'R': 
        #         dx, dy = dy, -dx
        #     if i == 'L':
        #         dx, dy = -dy, dx
        #     if i == 'G':
        #         x, y = x + dx, y + dy
        # return (x, y) == (0, 0) or (dx, dy) != (0, 1)


        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0

        for i in instructions:
            if i == 'L':
                idx = (idx + 3) % 4
            elif i == 'R':
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0
         

