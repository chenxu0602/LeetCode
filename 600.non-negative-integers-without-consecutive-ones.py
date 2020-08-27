#
# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (32.94%)
# Likes:    235
# Dislikes: 65
# Total Accepted:    9.1K
# Total Submissions: 27.5K
# Testcase Example:  '1'
#
# Given a positive integer n, find the number of non-negative integers less
# than or equal to n, whose binary representations do NOT contain consecutive
# ones.
# 
# Example 1:
# 
# Input: 5
# Output: 5
# Explanation: 
# Here are the non-negative integers 
# 
# 
# Note:
# 1 
# 
#
class Solution:
    def findIntegers(self, num: int) -> int:
        # O(log2(max_int)=32)

        f = [0] * 32
        f[0] = 1
        f[1] = 2

        for i in range(2, len(f)):
            f[i] = f[i-1] + f[i-2]

        i, s, prev_bit = 30, 0, 0
        while i >= 0:
            if num & (1 << i) != 0:
                s += f[i]
                if prev_bit == 1:
                    s -= 1
                    break

                prev_bit = 1

            else:
                prev_bit = 0

            i -= 1

        return s + 1



        # x, y are used to calculate Fibonacci numbers.
        # num & 1 and num & 2 will check if num ends with 11 in binary.
        # a(n) = the number of valid integers less than 2^n
        # a(5) = the number of valid integers less than 0b100000
        # It equals to the number of valid integers in [0b0, 0b10000[ and in [0b10000, 0b11000[.
        # The number of valid integers [0b0, 0b10000[, which is like '0b0XXXX', equals to a(4).
        # The number of valid integers [0b10000, 0b11000[, which is like '0b101XX', equals to a(3).
        # So a(5) = a(4) + a(3).
        # x , y = 1, 2
        # res = 0
        # num += 1
        # while num:
        #     if num & 1 and num & 2:
        #         res = 0
        #     res += x * (num & 1)
        #     num >>= 1
        #     x, y = y, x + y
        # return res
            



        
        

