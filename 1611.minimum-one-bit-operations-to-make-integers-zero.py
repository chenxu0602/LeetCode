#
# @lc app=leetcode id=1611 lang=python3
#
# [1611] Minimum One Bit Operations to Make Integers Zero
#
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/
#
# algorithms
# Hard (56.81%)
# Likes:    111
# Dislikes: 85
# Total Accepted:    3.1K
# Total Submissions: 5.4K
# Testcase Example:  '0'
#
# Given an integer n, you must transform it into 0 using the following
# operations any number of times:
# 
# 
# Change the rightmost (0^th) bit in the binary representation of n.
# Change the i^th bit in the binary representation of n if the (i-1)^th bit is
# set to 1 and the (i-2)^th through 0^th bits are set to 0.
# 
# 
# Return the minimum number of operations to transform n into 0.
# 
# 
# Example 1:
# 
# 
# Input: n = 0
# Output: 0
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 2
# Explanation: The binary representation of 3 is "11".
# "11" -> "01" with the 2nd operation since the 0th bit is 1.
# "01" -> "00" with the 1st operation.
# 
# 
# Example 3:
# 
# 
# Input: n = 6
# Output: 4
# Explanation: The binary representation of 6 is "110".
# "110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through
# 0th bits are 0.
# "010" -> "011" with the 1st operation.
# "011" -> "001" with the 2nd operation since the 0th bit is 1.
# "001" -> "000" with the 1st operation.
# 
# 
# Example 4:
# 
# 
# Input: n = 9
# Output: 14
# 
# 
# Example 5:
# 
# 
# Input: n = 333
# Output: 393
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Recursion
        # 2^k needs 2^(k+1) - 1 operations.
        # f(n) = f((b >> 1) ^ b ^ n) + 1 + b - 1,
        # where b is the maximum power of 2 that small or equals to n.
        # Time  complexity: O(nlogn)
        # Space complexity: O(nlogn)
        # self.dp = {0: 0}
        # if n not in self.dp:
        #     b = 1
        #     while (b << 1) <= n:
        #         b <<= 1
        #     self.dp[n] = self.minimumOneBitOperations((b >> 1) ^ b ^ n) + 1 + b - 1
        # return self.dp[n]


        # Iterative
        # We iterate the binary format of n, whenever we meet bit 1 at ith position,
        # we increment the result by (1 << (i + 1)) - 1.
        # Time  complexity: O(nlogn)
        # Space complexity: O(1)
        # res = 0
        # while n:
        #     res = -res - (n ^ (n - 1))
        #     n &= (n - 1)
        # return abs(res)


        # GrayCode
        res = 0
        while n > 0:
            res ^= n
            n >>= 1
        return res
        
# @lc code=end

