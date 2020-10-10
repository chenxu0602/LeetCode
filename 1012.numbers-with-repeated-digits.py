#
# @lc app=leetcode id=1012 lang=python3
#
# [1012] Numbers With Repeated Digits
#
# https://leetcode.com/problems/numbers-with-repeated-digits/description/
#
# algorithms
# Hard (37.42%)
# Likes:    223
# Dislikes: 45
# Total Accepted:    5.6K
# Total Submissions: 14.9K
# Testcase Example:  '20'
#
# Given a positive integer N, return the number of positive integers less than
# or equal to N that have at least 1 repeated digit.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 20
# Output: 1
# Explanation: The only positive number (<= 20) with at least 1 repeated digit
# is 11.
# 
# 
# 
# Example 2:
# 
# 
# Input: 100
# Output: 10
# Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are
# 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
# 
# 
# 
# Example 3:
# 
# 
# Input: 1000
# Output: 262
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 
# 
# 
#

# @lc code=start
class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        # if N = 8765, L = [8,7,6,6],
        # the number without repeated digit can the the following format:
        # XXX
        # XX
        # X
        # 1XXX ~ 7XXX
        # 80XX ~ 86XX
        # 870X ~ 875X
        # 8760 ~ 8765
        # Time  complexity: the number of permutations A(m,n) is O(1). We count digit by digit, so it's O(logN).
        L = list(map(int, str(N + 1)))
        res, n = 0, len(L)

        def A(m, n): # the permuation of m x (m - 1) x ... x (m - (n - 1))
            return 1 if n == 0 else A(m, n - 1) * (m - n + 1)

        for i in range(1, n):
            res += 9 * A(9, i - 1)

        s = set()
        for i, x in enumerate(L):
            for y in range(0 if i else 1, x):
                if y not in s:
                    res += A(9 - i, n - i - 1)
            if x in s: break
            s.add(x)

        return N - res
        
# @lc code=end

