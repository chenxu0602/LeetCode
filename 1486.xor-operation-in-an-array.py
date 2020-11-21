#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#
# https://leetcode.com/problems/xor-operation-in-an-array/description/
#
# algorithms
# Easy (84.02%)
# Likes:    288
# Dislikes: 156
# Total Accepted:    54.9K
# Total Submissions: 65.4K
# Testcase Example:  '5\n0'
#
# Given an integer n and an integer start.
# 
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n ==
# nums.length.
# 
# Return the bitwise XOR of all elements of nums.
# 
# 
# Example 1:
# 
# 
# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8)
# = 8.
# Where "^" corresponds to bitwise XOR operator.
# 
# 
# Example 2:
# 
# 
# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
# 
# Example 3:
# 
# 
# Input: n = 1, start = 7
# Output: 7
# 
# 
# Example 4:
# 
# 
# Input: n = 10, start = 5
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length
# 
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        last = start + 2 * (n - 1)
        if start % 4 < 2:
            start = 0
        else:
            n -= 1

        if n % 2 == 0: 
            return start ^ (n & 2)
        
        return start ^ last ^ (n & 2)
        
# @lc code=end

