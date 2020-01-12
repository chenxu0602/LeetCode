#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#
# https://leetcode.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (28.95%)
# Likes:    162
# Dislikes: 507
# Total Accepted:    28.3K
# Total Submissions: 97.7K
# Testcase Example:  '3\n5\n4'
#
# You are given two jugs with capacities x and y litres. There is an infinite
# amount of water supply available. You need to determine whether it is
# possible to measure exactly z litres using these two jugs.
# 
# If z liters of water is measurable, you must have z liters of water contained
# within one or both buckets by the end.
# 
# Operations allowed:
# 
# 
# Fill any of the jugs completely with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full or
# the first jug itself is empty.
# 
# 
# Example 1: (From the famous "Die Hard" example)
# 
# 
# Input: x = 3, y = 5, z = 4
# Output: True
# 
# 
# Example 2:
# 
# 
# Input: x = 2, y = 6, z = 5
# Output: False
# 
#
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        """
        a, b = x, y
        while y:
            r = x % y
            x = y
            y = r
            print(x, y, r)

        return bool(not z or (x and z <= a + b and z % x == 0))
        """

        def gcd(a, b):
            if a == 0: return b
            return gcd(b % a, a)

        if x > y: x, y = y, x
        gcd_res = gcd(x, y)
        if gcd_res == 0: return z == 0
        return z % gcd_res == 0 and z <= x + y
        

