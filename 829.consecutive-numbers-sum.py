#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#
# https://leetcode.com/problems/consecutive-numbers-sum/description/
#
# algorithms
# Hard (33.91%)
# Likes:    192
# Dislikes: 288
# Total Accepted:    13.5K
# Total Submissions: 39.4K
# Testcase Example:  '5'
#
# Given a positive integer N, how many ways can we write it as a sum of
# consecutive positive integers?
# 
# Example 1:
# 
# 
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# 
# Example 2:
# 
# 
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# 
# Example 3:
# 
# 
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# 
# Note: 1 <= N <= 10 ^ 9.
# 
#
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        """
        r = 1
        count = 0
        while r * (r-1) < 2 * N:
            if (N - (r * (r-1)) // 2) % r == 0:
                count += 1
            r += 1
        return count
        """

        res = 0
        i = 1
        while N > 0:
            res += (N % i == 0)
            N -= i
            i += 1
        return res

        

