#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.83%)
# Likes:    458
# Dislikes: 107
# Total Accepted:    113.2K
# Total Submissions: 283.5K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 1 + 3 + 5 + ... + (2n - 1)
        """
        if num < 0:
            return False

        x, i = 0, 1
        while x < num:
            x += i
            i += 2

        return x == num
        """

        root = 0
        bit = 1 << 15

        while bit > 0:
            root |= bit
            if root > num // root:
                root ^= bit
            bit >>= 1
        return root * root == num

        """
        r = num
        while r * r > num:
            r = (r + num / r) // 2

        return r * r == num
        """

        """
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1

        return False
        """


