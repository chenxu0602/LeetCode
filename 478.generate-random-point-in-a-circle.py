#
# @lc app=leetcode id=478 lang=python3
#
# [478] Generate Random Point in a Circle
#
# https://leetcode.com/problems/generate-random-point-in-a-circle/description/
#
# algorithms
# Medium (37.00%)
# Likes:    94
# Dislikes: 154
# Total Accepted:    5.7K
# Total Submissions: 15.5K
# Testcase Example:  '["Solution", "randPoint", "randPoint", ' +
#
# Given the radius and x-y positions of the center of a circle, write a
# function randPoint which generates a uniform random point in the circle.
# 
# Note:
# 
# 
# input and output values are in floating-point.
# radius and x-y position of the center of the circle is passed into the class
# constructor.
# a point on the circumference of the circle is considered to be in the
# circle.
# randPoint returns a size 2 array containing x-position and y-position of the
# random point, in that order.
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[10,5,-7.5],[],[],[]]
# Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has three arguments, the radius, x-position of the
# center, and y-position of the center of the circle. randPoint has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
# 
# 
#

import random, math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center
        

    def randPoint(self) -> List[float]:
        """
        while True:
            x = self.x + (2 * random.random() - 1) * self.radius
            y = self.y + (2 * random.random() - 1) * self.radius

            if (x-self.x)**2 + (y-self.y)**2 <= self.radius**2:
                return [x, y]
        """

        d = self.radius * math.sqrt(random.random())
        theta = random.random() * (2 * 3.1415926)
        return [self.x + d * math.cos(theta), self.y + d * math.sin(theta)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

