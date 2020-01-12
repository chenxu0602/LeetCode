#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (42.44%)
# Likes:    264
# Dislikes: 45
# Total Accepted:    15.1K
# Total Submissions: 35.4K
# Testcase Example:  '10'
#
# 
# Given a non-negative integer N, find the largest number that is less than or
# equal to N with monotone increasing digits.
# 
# (Recall that an integer has monotone increasing digits if and only if each
# pair of adjacent digits x and y satisfy x .)
# 
# 
# Example 1:
# 
# Input: N = 10
# Output: 9
# 
# 
# 
# Example 2:
# 
# Input: N = 1234
# Output: 1234
# 
# 
# 
# Example 3:
# 
# Input: N = 332
# Output: 299
# 
# 
# 
# Note:
# N is an integer in the range [0, 10^9].
# 
#
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        digits = []
        A = list(map(int, str(N)))
        for i in range(len(A)):
            for d in range(1, 10):
                if digits + [d] * (len(A)-i) > A:
                    digits.append(d-1)
                    break
            else:
                digits.append(9)

        return int("".join(map(str, digits)))
        """

        S = list(str(N))
        i = 1
        while i < len(S) and S[i-1] <= S[i]:
            i += 1
        while 0 < i < len(S) and S[i-1] > S[i]:
            S[i-1] = str(int(S[i-1]) - 1)
            i -= 1
        S[i+1:] = '9' * (len(S) - i - 1)
        return int("".join(S))
        

