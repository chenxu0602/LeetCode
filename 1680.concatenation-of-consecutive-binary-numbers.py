#
# @lc app=leetcode id=1680 lang=python3
#
# [1680] Concatenation of Consecutive Binary Numbers
#
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/
#
# algorithms
# Medium (43.99%)
# Likes:    55
# Dislikes: 81
# Total Accepted:    6.8K
# Total Submissions: 15.4K
# Testcase Example:  '1'
#
# Given an integer n, return the decimal value of the binary string formed by
# concatenating the binary representations of 1 to n in order, modulo 10^9 +
# 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 1
# Explanation: "1" in binary corresponds to the decimal value 1. 
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 27
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal
# value 27.
# 
# 
# Example 3:
# 
# 
# Input: n = 12
# Output: 505379714
# Explanation: The concatenation results in
# "1101110010111011110001001101010111100".
# The decimal value of that is 118505380540.
# After modulo 10^9 + 7, the result is 505379714.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# 
# 
#

# @lc code=start
import math

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # Time  complexity: O(nlogn)
        # Space complexity: O(nlogn)
        # MOD = 10**9 + 7
        # concatenation = "".join(bin(i)[2:] for i in range(n + 1))
        # return int(concatenation, 2) % MOD

        # Time  complexity: O(nlogn)
        # Space complexity: O(1)
        # MOD = 10**9 + 7
        # length, result = 0, 0
        # for i in range(1, n + 1):
        #     # when meets power of 2, increase the bit length
        #     if math.log(i, 2).is_integer():
        #         length += 1
        #     result = ((result * (2 ** length)) + i) % MOD
        # return result


        # Time  complexity: O(n)
        # Space complexity: O(1)
        MOD = 10**9 + 7
        length, result = 0, 0
        for i in range(1, n + 1):
            # when meets power of 2, increase the bit length
            if i & (i - 1) == 0:
                length += 1
            result = ((result << length) | i) % MOD
        return result

        
# @lc code=end

