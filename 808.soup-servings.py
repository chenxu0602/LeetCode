#
# @lc app=leetcode id=808 lang=python3
#
# [808] Soup Servings
#
# https://leetcode.com/problems/soup-servings/description/
#
# algorithms
# Medium (38.04%)
# Likes:    102
# Dislikes: 377
# Total Accepted:    6.9K
# Total Submissions: 18.1K
# Testcase Example:  '50'
#
# There are two types of soup: type A and type B. Initially we have N ml of
# each type of soup. There are four kinds of operations:
# 
# 
# Serve 100 ml of soup A and 0 ml of soup B
# Serve 75 ml of soup A and 25 ml of soup B
# Serve 50 ml of soup A and 50 ml of soup B
# Serve 25 ml of soup A and 75 ml of soup B
# 
# 
# When we serve some soup, we give it to someone and we no longer have it.
# Each turn, we will choose from the four operations with equal probability
# 0.25. If the remaining volume of soup is not enough to complete the
# operation, we will serve as much as we can.  We stop once we no longer have
# some quantity of both types of soup.
# 
# Note that we do not have the operation where all 100 ml's of soup B are used
# first.  
# 
# Return the probability that soup A will be empty first, plus half the
# probability that A and B become empty at the same time.
# 
# 
# 
# 
# Example:
# Input: N = 50
# Output: 0.625
# Explanation: 
# If we choose the first two operations, A will become empty first. For the
# third operation, A and B will become empty at the same time. For the fourth
# operation, B will become empty first. So the total probability of A becoming
# empty first plus half the probability that A and B become empty at the same
# time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
# 
# 
# 
# Notes: 
# 
# 
# 0 <= N <= 10^9. 
# Answers within 10^-6 of the true value will be accepted as correct.
# 
# 
#
class Solution:
    def soupServings(self, N: int) -> float:
        if N > 500 * 25: return 1

        memo = {}

        def dp(n1, n2, memo):
            if n1 <= 0 and n2 <= 0:
                return 0.5
            if n1 <= 0:
                return 1.0
            if n2 <= 0:
                return 0

            if (n1, n2) in memo:
                return memo[(n1, n2)]

            memo[(n1, n2)] = 0.25 * (dp(n1-100, n2, memo) + dp(n1-75, n2-25, memo) + dp(n1-50, n2-50, memo) + dp(n1-25, n2-75, memo))
            return memo[(n1, n2)]
        
        prob = dp(N, N, memo)
        return round(prob, 5)


