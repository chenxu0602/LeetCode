#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (42.77%)
# Likes:    1788
# Dislikes: 154
# Total Accepted:    216.7K
# Total Submissions: 500.3K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

# @lc code=start
from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:

        """
        dp = [0] * (n+1)
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = 1 + min(dp[i-j*j] for j in range(1, int(sqrt(i)+1)))

        return dp[-1]
        """

        if n < 2: return n
        lst = []
        i = 0
        while i * i <= n:
            lst.append(i*i)
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp
        
        return cnt
