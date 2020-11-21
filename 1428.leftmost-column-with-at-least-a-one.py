#
# @lc app=leetcode id=1428 lang=python3
#
# [1428] Leftmost Column with at Least a One
#
# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/description/
#
# algorithms
# Medium (48.14%)
# Likes:    277
# Dislikes: 32
# Total Accepted:    65.9K
# Total Submissions: 136.8K
# Testcase Example:  '[[0,0],[1,1]]'
#
# (This problem is an interactive problem.)
# 
# A binary matrix means that all elements are 0 or 1. For each individual row
# of the matrix, this row is sorted in non-decreasing order.
# 
# Given a row-sorted binary matrix binaryMatrix, return leftmost column
# index(0-indexed) with at least a 1 in it. If such index doesn't exist, return
# -1.
# 
# You can't access the Binary Matrix directly.  You may only access the matrix
# using a BinaryMatrix interface:
# 
# 
# BinaryMatrix.get(row, col) returns the element of the matrix at index (row,
# col) (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which
# means the matrix is rows * cols.
# 
# 
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged
# Wrong Answer.  Also, any solutions that attempt to circumvent the judge will
# result in disqualification.
# 
# For custom testing purposes you're given the binary matrix mat as input in
# the following four examples. You will not have access the binary matrix
# directly.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: mat = [[0,0],[1,1]]
# Output: 0
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: mat = [[0,0],[0,1]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: mat = [[0,0],[0,0]]
# Output: -1
# 
# Example 4:
# 
# 
# 
# 
# Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] is either 0 or 1.
# mat[i] is sorted in a non-decreasing way.
# 
# 
#

# @lc code=start
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        # Time  complexity: O(M + N)
        # Space complexity: O(1)
        # rows, cols = binaryMatrix.dimensions()

        # current_row, current_col = 0, cols - 1

        # while current_row < rows and current_col >= 0:
        #     if binaryMatrix.get(current_row, current_col) == 0:
        #         current_row += 1
        #     else:
        #         current_col -= 1

        # return current_col + 1 if current_col != cols - 1 else -1


        # Time  complexity: O(NlogM)
        # Space complexity: O(1)
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols
        for row in range(rows):
            lo, hi = 0, cols - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid

            if binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)
            
        return -1 if smallest_index == cols else smallest_index
        
# @lc code=end

