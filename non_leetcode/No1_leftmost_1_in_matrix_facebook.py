#!/usr/bin/python
# coding=utf-8
################################################################################
'''
In a binary matrix (all elements are 0 and 1), every row is sorted in
ascending order (0 to the left of 1). Find the leftmost column index with a 1 in it.

Example 1:

Input:
[[0, 0, 0, 1],
 [0, 0, 1, 1],
 [0, 1, 1, 1],
 [0, 0, 0, 0]]
Output: 1
Example 2:

Input:
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
Output: -1
Expected solution better than O(r * c).

Solution
Similar questions:
'''
################################################################################

'''
Method1:
Handle degenerate case of all 0s separately.
Start from top right. Keep doing until we reach last row: go down if current element is 0, go left otherwise.
Column number of final ptr is our answer.
Time complexity - O(M+N)
'''

class Solution(object):
    def find_leftmost_column(self, matrix):

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        row, col = 0, len(matrix[0]) - 1
        M = len(matrix)
        N = len(matrix[0])

        while row < M and col >= 0:
            if matrix[row][col] == 1:
                col -= 1
            else:
                row += 1

        #NOTE: be careful about here
        if col < 0:
            return 0
        elif col == N - 1:
            return -1
        else:
            return col + 1


a = Solution()
print a.find_leftmost_column([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1],[0, 0, 0, 0]])
print a.find_leftmost_column([[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]])



'''
Method2:
binary search for each column
'''
