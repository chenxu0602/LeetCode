#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.34%)
# Likes:    260
# Dislikes: 842
# Total Accepted:    48.5K
# Total Submissions: 159.5K
# Testcase Example:  '3'
#
# Find the n^th digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 2^31).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution:
    def findNthDigit(self, n: int) -> int:
        # The first elements of these groups are 1, 10, 100, 1000...has the form 10**(digits-1) for digits in range(1, 11) (11 is big enough to cover all n in the given range). But how do we determine the group from n? Notice the groups has 9, 90, 900, 9000...elements and the total number of digits in the groups are 1＊9, 2＊90, 3＊900, 4＊9000.....Let's formalize the observation. For the digits-th group,
        # first = the first element 9 * first = the size of the group 9 * first * digits = the number of digits in the group
        n -= 1
        for digits in range(1, 11):
            first = 10 ** (digits - 1)
            if n < 9 * first * digits:
                return int(str(first + (n // digits))[n % digits])
            n -= 9 * first * digits
        

