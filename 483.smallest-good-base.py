#
# @lc app=leetcode id=483 lang=python3
#
# [483] Smallest Good Base
#
# https://leetcode.com/problems/smallest-good-base/description/
#
# algorithms
# Hard (34.28%)
# Likes:    89
# Dislikes: 251
# Total Accepted:    10.1K
# Total Submissions: 29.5K
# Testcase Example:  '"13"'
#
# For an integer n, we call k>=2 a good base of n, if all digits of n base k
# are 1.
# 
# Now given a string representing n, you should return the smallest good base
# of n in string format.
# 
# Example 1:
# 
# 
# Input: "13"
# Output: "3"
# Explanation: 13 base 3 is 111.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
# 
# 
# 
# 
# Note:
# 
# 
# The range of n is [3, 10^18].
# The string representing n is always valid and will not have leading
# zeros.
# 
# 
# 
# 
#
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_len = len(bin(n)) - 2
        for m in range(max_len, 1, -1):
            lo, hi = 2, n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                num = (pow(mid, m) - 1) // (mid - 1)
                if num < n:
                    lo = mid + 1
                elif num > n:
                    hi = mid - 1
                else:
                    return str(mid)

        return str(n-1)
        

