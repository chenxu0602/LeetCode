#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (36.36%)
# Likes:    508
# Dislikes: 69
# Total Accepted:    90K
# Total Submissions: 245.3K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
# 
# Example 1:
# 
# 
# Input: [5,7]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: [0,1]
# Output: 0
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i

        """
        while m < n:
            n = n & (n-1)
        return n
        """
        
# @lc code=end

