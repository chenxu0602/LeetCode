#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#
# https://leetcode.com/problems/complement-of-base-10-integer/description/
#
# algorithms
# Easy (59.55%)
# Likes:    323
# Dislikes: 38
# Total Accepted:    46.5K
# Total Submissions: 76K
# Testcase Example:  '5'
#
# Every non-negative integer N has a binary representation.  For example, 5 can
# be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note
# that except for N = 0, there are no leading zeroes in any binary
# representation.
# 
# The complement of a binary representation is the number in binary you get
# when changing every 1 to a 0 and 0 to a 1.  For example, the complement of
# "101" in binary is "010" in binary.
# 
# For a given number N in base-10, return the complement of it's binary
# representation as a base-10 integer.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is
# 2 in base-10.
# 
# 
# 
# Example 2:
# 
# 
# Input: 7
# Output: 0
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is
# 0 in base-10.
# 
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: 5
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which
# is 5 in base-10.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= N < 10^9
# This question is the same as 476:
# https://leetcode.com/problems/number-complement/
# 
# 
# 
# 
# 
#

# @lc code=start
import math

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # Flip Bit By Bit
        # Time  complexity: O(1), since we're doing not more than 32 iterations here.
        # Space complexity: O(1)
        # if N == 0:
        #     return 1
        # todo, bit = N, 1
        # while todo:
        #     N = N ^ bit
        #     bit = bit << 1
        #     todo = todo >> 1
        # return N


        # Compute Bit Length and Construct 1-bits Bitmask
        # O(1)
        # if N == 0: 
        #     return 1
        # # l is a length of N in binary representation
        # l = math.floor(math.log2(N)) + 1
        # # bitmask has the same length as N and contains only ones 1...1
        # bitmask = (1 << l) - 1
        # # flip all bits
        # return bitmask ^ N


        # X = 1
        # while N > X:
        #     X = X * 2 + 1
        # return N ^ X


        return (1 << N.bit_length()) - N - 1 if N else 1



        
# @lc code=end

