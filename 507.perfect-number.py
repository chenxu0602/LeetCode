#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (34.62%)
# Likes:    161
# Dislikes: 460
# Total Accepted:    43.8K
# Total Submissions: 126.3K
# Testcase Example:  '28'
#
# We define the Perfect Number is a positive integer that is equal to the sum
# of all its positive divisors except itself. 
# 
# Now, given an integer n, write a function that returns true when it is a
# perfect number and false when it is not.
# 
# 
# Example:
# 
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 
# 
# 
# Note:
# The input number n will not exceed 100,000,000. (1e8)
# 
#
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        if num <= 1: return False

        s, q = 0, num**.5
        for i in range(2, 1+int(q)):
            if num % i == 0:
                s += i + num // i
        if int(q) == q:
            s -= 1
        return s == num - 1
        """

        if num <= 0: return False
        s, i = 0, 1
        while i * i <= num:
            if num % i == 0:
                s += i
                if i * i != num:
                    s += num // i
            i += 1

        return s - num == num

        

