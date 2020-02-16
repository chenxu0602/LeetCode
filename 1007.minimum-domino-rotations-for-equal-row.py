#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/
#
# algorithms
# Medium (48.89%)
# Likes:    180
# Dislikes: 90
# Total Accepted:    23K
# Total Submissions: 44.8K
# Testcase Example:  '[2,1,2,4,2,2]\n[5,2,6,2,3,2]'
#
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of
# the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on
# each half of the tile.)
# 
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
# 
# Return the minimum number of rotations so that all the values in A are the
# same, or all the values in B are the same.
# 
# If it cannot be done, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by A and B: before we do
# any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the
# top row equal to 2, as indicated by the second figure.
# 
# 
# Example 2:
# 
# 
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of
# values equal.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A[i], B[i] <= 6
# 2 <= A.length == B.length <= 20000
# 
# 
#
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # candidates = set([A[0]] + [B[0]])

        # for i in range(1, len(A)):
        #     next_col = set([A[i]] + [B[i]])
        #     candidates = candidates.intersection(next_col)
        #     if not candidates:
        #         return -1

        # res = float("inf")
        # for cand in candidates:
        #     top, bottom = 0, 0
        #     for i in range(len(A)):
        #         top += A[i] == cand
        #         bottom += B[i] == cand
        #     res = min(res, len(A) - max(top, bottom))
        # return res


        # for x in range(1, 7):
        #     if all(x in d for d in zip(A, B)):
        #         return len(A) - max(A.count(x), B.count(x))
        # return -1


        from functools import reduce
        s = reduce(set.__and__, [set(d) for d in zip(A, B)])
        if not s: return -1
        x = s.pop()
        return len(A) - max(A.count(x), B.count(x))
        

