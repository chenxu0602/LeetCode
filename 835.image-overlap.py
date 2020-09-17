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
        # Linear Transformation
        # Time  complexity: O(N^4)
        # Space complexity: O(N^2)
        # R = len(A)
        # C = len(A[0])
        # la = []
        # lb = []

        # v = Counter()

        # for r in range(R):
        #     for c in range(C):
        #         if A[r][c] == 1:
        #             la.append((r, c))
        #         if B[r][c] == 1:
        #             lb.append((r, c))

        # for ax, ay in la:
        #     for bx, by in lb:
        #         k = (ax-bx, ay-by)
        #         v[k] += 1

        # return max(v.values() or [0])


        # Image Convolution
        # First of all, we extend both the width and height of the matrix B to N + 2(N-1) = 3N-2N+2(N−1)=3N−2, and pad the extended cells with zeros.
        # From the extended and padded matrix B, we then can extract the kernel one by one.
        # For each kernel, we perform the convolution operation with the matrix A to count the number of overlapping ones.
        # Time  complexity: O(N^4)
        # Space complexity: O(N^2)
        import numpy as np
        A, B = np.array(A), np.array(B)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim - 1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim * 2 - 1):
            for y_shift in range(dim * 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift + dim, y_shift:y_shift + dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps
        

