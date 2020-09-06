#
# @lc app=leetcode id=805 lang=python3
#
# [805] Split Array With Same Average
#
# https://leetcode.com/problems/split-array-with-same-average/description/
#
# algorithms
# Hard (24.71%)
# Likes:    244
# Dislikes: 49
# Total Accepted:    10.3K
# Total Submissions: 41.6K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# In a given integer array A, we must move every element of A to either list B
# or list C. (B and C initially start empty.)
# 
# Return true if and only if after such a move, it is possible that the average
# value of B is equal to the average value of C, and B and C are both
# non-empty.
# 
# 
# Example :
# Input: 
# [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of
# them have the average of 4.5.
# 
# 
# Note:
# 
# 
# The length of A will be in the range [1, 30].
# A[i] will be in the range of [0, 10000].
# 
# 
# 
# 
#
from fractions import Fraction
from functools import lru_cache

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        # Time  complexity: O(2^(N/2))
        # Space complexity: O(2^(N/2))
        # N, S = len(A), sum(A)
        # A = [z - Fraction(S, N) for z in A]

        # if N == 1: return False

        # left = {A[0]}
        # for i in range(1, N//2):
        #     left = {z + A[i] for z in left} | left | {A[i]}
        # if 0 in left: return True

        # right = {A[-1]}
        # for i in range(N//2, N-1):
        #     right = {z + A[i] for z in right} | right | {A[i]}
        # if 0 in right: return True

        # sleft = sum(A[i] for i in range(N//2))
        # sright = sum(A[i] for i in range(N//2, N))

        # return any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left)



        @lru_cache(None)
        def find(target, k, i):
            if k == 0: return target == 0
            if target < 0 or k + i > n: return False
            return find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)

        n, s = len(A), sum(A)
        return any(find(s * k // n, k, 0) for k in range(1, n // 2 + 1) if s * k % n == 0)


        

