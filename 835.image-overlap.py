#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#
# https://leetcode.com/problems/image-overlap/description/
#
# algorithms
# Medium (53.69%)
# Likes:    213
# Dislikes: 293
# Total Accepted:    12.9K
# Total Submissions: 23.9K
# Testcase Example:  '[[1,1,0],[0,1,0],[0,1,0]]\n[[0,0,0],[0,1,1],[0,0,1]]'
#
# Two images A and B are given, represented as binary, square matrices of the
# same size.  (A binary matrix has only 0s and 1s as values.)
# 
# We translate one image however we choose (sliding it left, right, up, or down
# any number of units), and place it on top of the other image.  After, the
# overlap of this translation is the number of positions that have a 1 in both
# images.
# 
# (Note also that a translation does not include any kind of rotation.)
# 
# What is the largest possible overlap?
# 
# Example 1:
# 
# 
# Input: A = [[1,1,0],
# ⁠           [0,1,0],
# [0,1,0]]
# B = [[0,0,0],
# [0,1,1],
# [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
# 
# Notes: 
# 
# 
# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1
# 
# 
#
from collections import Counter

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        R = len(A)
        C = len(A[0])
        la = []
        lb = []

        v = Counter()

        for r in range(R):
            for c in range(C):
                if A[r][c] == 1:
                    la.append((r, c))
                if B[r][c] == 1:
                    lb.append((r, c))

        for ax, ay in la:
            for bx, by in lb:
                k = (ax-bx, ay-by)
                v[k] += 1

        return max(v.values() or [0])
        

