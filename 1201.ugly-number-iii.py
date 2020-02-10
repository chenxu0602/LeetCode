#
# @lc app=leetcode id=1201 lang=python3
#
# [1201] Ugly Number III
#
# https://leetcode.com/problems/ugly-number-iii/description/
#
# algorithms
# Medium (24.95%)
# Likes:    134
# Dislikes: 156
# Total Accepted:    6.1K
# Total Submissions: 24.4K
# Testcase Example:  '3\n2\n3\n5'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive integers which are divisible by a or b or c.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, a = 2, b = 3, c = 5
# Output: 4
# Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
# 
# Example 2:
# 
# 
# Input: n = 4, a = 2, b = 3, c = 4
# Output: 6
# Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
# 
# 
# Example 3:
# 
# 
# Input: n = 5, a = 2, b = 11, c = 13
# Output: 10
# Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is
# 10.
# 
# 
# Example 4:
# 
# 
# Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
# Output: 1999999984
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n, a, b, c <= 10^9
# 1 <= a * b * c <= 10^18
# It's guaranteed that the result will be in range [1, 2 * 10^9]
# 
# 
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)

        def lcm(a, b):
            return a * b // gcd(a, b)

        def count(num, a, b, c):
            return num//a + num//b + num//c - num//lcm(a, b) - num//lcm(b, c) - num//lcm(a, c) + num//lcm(lcm(a, b), c)

        left, right = 1, n * min(a, b, c)
        while left < right:
            mid = left + (right - left) // 2
            if count(mid, a, b, c) < n:
                left = mid + 1
            else:
                right = mid

        return left
        
# @lc code=end

