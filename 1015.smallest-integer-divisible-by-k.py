#
# @lc app=leetcode id=1015 lang=python3
#
# [1015] Smallest Integer Divisible by K
#
# https://leetcode.com/problems/smallest-integer-divisible-by-k/description/
#
# algorithms
# Medium (29.30%)
# Likes:    62
# Dislikes: 190
# Total Accepted:    7K
# Total Submissions: 23.4K
# Testcase Example:  '1'
#
# Given a positive integer K, you need find the smallest positive integer N
# such that N is divisible by K, and N only contains the digit 1.
# 
# Return the length of N.  If there is no such N, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: 1
# Explanation: The smallest answer is N = 1, which has length 1.
# 
# Example 2:
# 
# 
# Input: 2
# Output: -1
# Explanation: There is no such positive integer N divisible by 2.
# 
# Example 3:
# 
# 
# Input: 3
# Output: 3
# Explanation: The smallest answer is N = 111, which has length 3.
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= 10^5
# 
#
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 10 not in {1, 3, 7, 9}:
            return -1

        mod, mod_set = 0, set()
        for length in range(1, K+1):
            mod = (10 * mod + 1) % K
            if mod == 0:
                return length
            if mod in mod_set:
                return -1
            mod_set.add(mod)
        return -1
        

