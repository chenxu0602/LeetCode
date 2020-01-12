#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#
# https://leetcode.com/problems/rotated-digits/description/
#
# algorithms
# Easy (54.98%)
# Likes:    224
# Dislikes: 765
# Total Accepted:    32.3K
# Total Submissions: 58.6K
# Testcase Example:  '10'
#
# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.  Each digit must be rotated -
# we cannot choose to leave it alone.
# 
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8
# rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each
# other, and the rest of the numbers do not rotate to any other number and
# become invalid.
# 
# Now given a positive number N, how many numbers X from 1 to N are good?
# 
# 
# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
# 
# 
# Note:
# 
# 
# N  will be in range [1, 10000].
# 
# 
#
class Solution:
    def rotatedDigits(self, N: int) -> int:
        """
        ans = 0
        for x in range(1, N+1):
            S = str(x)
            ans += (all(d not in "347" for d in S) and any(d in "2569" for d in S))
        return ans
        """

        N, t, c = str(N), 0, 1
        L, a, b = len(N) - 1, [1,2,3,3,3,4,5,5,6,7], [1,2,2,2,2,2,2,2,3,3] 
    	
        for i in range(L):
            if N[i] == '0': continue
            t += a[int(N[i])-1]*7**(L-i) - c*b[int(N[i])-1]*3**(L-i)
            if N[i] in '347': return t
            if N[i] not in '18': c = 0
        return t + a[int(N[-1])] - c*b[int(N[-1])]


