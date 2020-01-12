#
# @lc app=leetcode id=1088 lang=python3
#
# [1088] Confusing Number II
#
# https://leetcode.com/problems/confusing-number-ii/description/
#
# algorithms
# Hard (36.12%)
# Likes:    25
# Dislikes: 8
# Total Accepted:    1.5K
# Total Submissions: 4.4K
# Testcase Example:  '20'
#
# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9
# are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3,
# 4, 5 and 7 are rotated 180 degrees, they become invalid.
# 
# A confusing number is a number that when rotated 180 degrees becomes a
# different number with each digit valid.(Note that the rotated number can be
# greater than the original number.)
# 
# Given a positive integer N, return the number of confusing numbers between 1
# and N inclusive.
# 
# 
# 
# Example 1:
# 
# 
# Input: 20
# Output: 6
# Explanation: 
# The confusing numbers are [6,9,10,16,18,19].
# 6 converts to 9.
# 9 converts to 6.
# 10 converts to 01 which is just 1.
# 16 converts to 91.
# 18 converts to 81.
# 19 converts to 61.
# 
# 
# Example 2:
# 
# 
# Input: 100
# Output: 19
# Explanation: 
# The confusing numbers are
# [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 
#
class Solution:
    count = 0
    n = 0

    def confusingNumberII(self, N: int) -> int:
        self.n = N
        self.search(0)
        return self.count

    def search(self, i):
        if i > self.n:
            return

        if i != 0:
            if self.is_confusing(i):
                self.count += 1
            self.search(i*10)

        self.search(i*10 + 1)
        self.search(i*10 + 6)
        self.search(i*10 + 8)
        self.search(i*10 + 9)

    def is_confusing(self, x):
        rot, orig = 0, x
        while x:
            x, r = divmod(x, 10)
            if r == 6:
                r = 9
            elif r == 9:
                r = 6
            rot = rot * 10 + r
        return True if rot != orig else False

