#
# @lc app=leetcode id=1414 lang=python3
#
# [1414] Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
#
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/description/
#
# algorithms
# Medium (63.47%)
# Likes:    292
# Dislikes: 34
# Total Accepted:    16.9K
# Total Submissions: 26.6K
# Testcase Example:  '7'
#
# Given an integer k, return the minimum number of Fibonacci numbers whose sum
# is equal to k. The same Fibonacci number can be used multiple times.
# 
# The Fibonacci numbers are defined as:
# 
# 
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 for n > 2.
# 
# It is guaranteed that for the given constraints we can always find such
# Fibonacci numbers that sum up to k.
# 
# Example 1:
# 
# 
# Input: k = 7
# Output: 2 
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
# For k = 7 we can use 2 + 5 = 7.
# 
# Example 2:
# 
# 
# Input: k = 10
# Output: 2 
# Explanation: For k = 10 we can use 2 + 8 = 10.
# 
# 
# Example 3:
# 
# 
# Input: k = 19
# Output: 3 
# Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Time  complexity: O((logk) ^ 2)
        # Space compleixty: O(logk)
        # if k < 2: return k
        # a, b = 1, 1
        # while b <= k:
        #     a, b = b, a + b
        # return self.findMinFibonacciNumbers(k - a) + 1

        # Time  complexity: O(logk)
        # Space compleixty: O(logk)
        res, a, b = 0, 1, 1
        while b <= k:
            a, b = b, a + b
        while a > 0:
            if a <= k:
                k -= a
                res += 1
            a, b = b - a, a
        return res
        
# @lc code=end

