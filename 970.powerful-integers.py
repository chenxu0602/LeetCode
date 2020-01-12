#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#
# https://leetcode.com/problems/powerful-integers/description/
#
# algorithms
# Easy (39.46%)
# Likes:    82
# Dislikes: 184
# Total Accepted:    14.5K
# Total Submissions: 36.6K
# Testcase Example:  '2\n3\n10'
#
# Given two positive integers x and y, an integer is powerful if it is equal to
# x^i + y^j for some integers i >= 0 and j >= 0.
# 
# Return a list of all powerful integers that have value less than or equal to
# bound.
# 
# You may return the answer in any order.  In your answer, each value should
# occur at most once.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation: 
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
# 
# 
# 
# Example 2:
# 
# 
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6
# 
#
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xpow = []
        if x == 1:
            xpow = [1]
        else:
            _x = 1
            while _x < bound:
                xpow.append(_x)
                _x *= x

        ypow = []
        if y == 1:
            ypow = [1]
        else:
            _y = 1
            while _y < bound:
                ypow.append(_y)
                _y *= y

        s = set([x+y for x in xpow for y in ypow if x+y <= bound])
        return list(s)
        

