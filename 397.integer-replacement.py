#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (31.44%)
# Likes:    216
# Dislikes: 243
# Total Accepted:    41.5K
# Total Submissions: 131.6K
# Testcase Example:  '8'
#
# 
# Given a positive integer n and you can do operations as follow:
# 
# 
# 
# 
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# 
# 
# 
# 
# What is the minimum number of replacements needed for n to become 1?
# 
# 
# 
# 
# Example 1:
# 
# Input:
# 8
# 
# Output:
# 3
# 
# Explanation:
# 8 -> 4 -> 2 -> 1
# 
# 
# 
# Example 2:
# 
# Input:
# 7
# 
# Output:
# 4
# 
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
# 
# 
#
class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while not n == 1:
            if bin(n)[-1] == '0':
                n >>= 1
            else:
                if bin(n)[-2] == '1' and not len(bin(n)) == 4:
                    n += 1
                else:
                    n -= 1
            res += 1
        
        return res

