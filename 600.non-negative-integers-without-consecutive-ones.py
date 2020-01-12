#
# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (32.94%)
# Likes:    235
# Dislikes: 65
# Total Accepted:    9.1K
# Total Submissions: 27.5K
# Testcase Example:  '1'
#
# Given a positive integer n, find the number of non-negative integers less
# than or equal to n, whose binary representations do NOT contain consecutive
# ones.
# 
# Example 1:
# 
# Input: 5
# Output: 5
# Explanation: 
# Here are the non-negative integers 
# 
# 
# Note:
# 1 
# 
#
class Solution:
    def findIntegers(self, num: int) -> int:
        """
        f = [0] * 32
        f[0] = 1
        f[1] = 2

        for i in range(2, len(f)):
            f[i] = f[i-1] + f[i-2]

        i, s, prev_bit = 30, 0, 0
        while i >= 0:
            if num & (1 << i) != 0:
                s += f[i]
                if prev_bit == 1:
                    s -= 1
                    break

                prev_bit = 1

            else:
                prev_bit = 0

            i -= 1

        return s + 1
        """

        A = bin(num)[2:][::-1]
        dp = [[1, 1] for _ in range(len(A))]
        res = 1 if A[0] == '0' else 2
        for i in range(1, len(A)):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]

            if A[i-1:i+1] == "01":
                res += dp[i][0]
            elif A[i-1:i+1] == "11":
                res = dp[i][0] + dp[i][1]
                
        return res




        
        

