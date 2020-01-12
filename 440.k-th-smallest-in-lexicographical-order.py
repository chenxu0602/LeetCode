#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (26.67%)
# Likes:    179
# Dislikes: 33
# Total Accepted:    8.5K
# Total Submissions: 31.9K
# Testcase Example:  '13\n2'
#
# Given integers n and k, find the lexicographically k-th smallest integer in
# the range from 1 to n.
# 
# Note: 1 ≤ k ≤ n ≤ 10^9.
# 
# Example:
# 
# Input:
# n: 13   k: 2
# 
# Output:
# 10
# 
# Explanation:
# The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so
# the second smallest number is 10.
# 
# 
# 
#
class Solution:
    def calc_steps(self, n, n1, n2):
        steps = 0

        while n1 <= n:
            steps += min(n+1, n2) - n1
            n1 *= 10
            n2 *= 10

        return steps

    def findKthNumber(self, n: int, k: int) -> int:

        curr, k = 1, k - 1
        while k > 0:
            steps = self.calc_steps(n, curr, curr+1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr
        

