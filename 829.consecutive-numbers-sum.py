#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#
# https://leetcode.com/problems/consecutive-numbers-sum/description/
#
# algorithms
# Hard (36.92%)
# Likes:    364
# Dislikes: 488
# Total Accepted:    25.8K
# Total Submissions: 67.9K
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

# @lc code=start
import math

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # N = xk + k(k+1)/2
        # x = N/k - (k+1)/2
        # k <= sqrt(2N + 1/4) - 1/2
        # Time  complexity: O(sqrt(N))
        # Space compleixty: O(1)
        # count = 0
        # upper_limit = math.ceil((2 * N + 0.25)**0.5 - 0.5) + 1
        # for k in range(1, upper_limit):
        #     if (N - k * (k + 1) // 2) % k == 0:
        #         count += 1
        # return count


        count = 0
        upper_limit = math.ceil((2 * N + 0.25) ** 0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            N -= k
            if N % k == 0:
                count += 1
        return count
        
# @lc code=end

