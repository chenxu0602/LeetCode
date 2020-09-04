#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (49.69%)
# Likes:    785
# Dislikes: 53
# Total Accepted:    73.3K
# Total Submissions: 148K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# We are given two strings, A and B.
# 
# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.
# 
# 
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
# 
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# 
# 
# Note:
# 
# 
# A and B will have length at most 100.
# 
# 
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        # return len(A) == len(B) and B in A + A

        # Rolling Hash
        # O(N)
        # MOD = 10**9 + 7
        # P = 113
        # Pinv = pow(P, MOD-2, MOD)

        # hb, power = 0, 1
        # for x in B:
        #     code = ord(x) - 96
        #     hb = (hb + power * code) % MOD
        #     power = power * P % MOD
        
        # ha, power = 0, 1
        # for x in A:
        #     code = ord(x) - 96
        #     ha = (ha + power * code) % MOD
        #     power = power * P % MOD

        # if ha == hb and A == B: return True

        # for i, x in enumerate(A):
        #     code = ord(x) - 96
        #     ha += power * code
        #     ha -= code
        #     ha *= Pinv
        #     ha %= MOD
        #     if ha == hb and A[i+1:] + A[:i+1] == B:
        #         return True
        # return False


        # KMP (Knuth-Morris-Pratt)
        # O(N)
        N = len(A)
        if N != len(B): return False
        if N == 0: return True

        # Compute the shift table
        shifts = [1] * (N + 1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1

        # Find match of B in A + A
        match_len = 0
        for char in A + A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False
# @lc code=end

