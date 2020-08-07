#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (39.33%)
# Likes:    1043
# Dislikes: 124
# Total Accepted:    155.1K
# Total Submissions: 394.4K
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
        # Bit Shift
        # Time  complexity: O(1)
        # Space complexity: O(1)
        # shift = 0
        # while m != n:
        #     m >>= 1
        #     n >>= 1
        #     shift += 1
        # return n << shift


        # Brian Kernighan's Algorithm
        # Time  complexity: O(1)
        # Space complexity: O(1)
        while m < n:
            n = n & (n - 1)
        return n

        
# @lc code=end

