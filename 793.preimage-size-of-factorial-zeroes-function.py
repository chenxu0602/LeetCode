#
# @lc app=leetcode id=793 lang=python3
#
# [793] Preimage Size of Factorial Zeroes Function
#
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/description/
#
# algorithms
# Hard (39.21%)
# Likes:    113
# Dislikes: 46
# Total Accepted:    6K
# Total Submissions: 15.3K
# Testcase Example:  '0'
#
# Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 *
# 3 * ... * x, and by convention, 0! = 1.)
# 
# For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) =
# 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many
# non-negative integers x have the property that f(x) = K.
# 
# 
# Example 1:
# Input: K = 0
# Output: 5
# Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.
# 
# Example 2:
# Input: K = 5
# Output: 0
# Explanation: There is no x such that x! ends in K = 5 zeroes.
# 
# 
# Note:
# 
# 
# K will be an integer in the range [0, 10^9].
# 
# 
#
class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def zeta(x):
            return x // 5 + zeta(x // 5) if x > 0 else 0

        lo, hi = K, 10*K + 1
        while lo < hi:
            mi = (lo + hi) // 2
            zmi = zeta(mi)
            if zmi == K:
                return 5
            elif zmi < K:
                lo = mi + 1
            else:
                hi = mi
        return 0
        

