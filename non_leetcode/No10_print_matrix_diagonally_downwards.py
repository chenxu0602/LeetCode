#!/usr/bin/python
# coding=utf-8
################################################################################
'''
https://www.geeksforgeeks.org/print-the-matrix-diagonally-downwards/
Given a matrix of size n*n, print the matrix in the following pattern.


Output: 1 2 5 3 6 9 4 7 10 13 8 11 14 12 15 16

Examples:





Input :matrix[2][2]= { {1, 2},
                       {3, 4} }
Output : 1 2 3 4

Input :matrix[3][3]= { {1, 2, 3},
                       {4, 5, 6},
                       {7, 8, 9} }
Output : 1 2 4 3 5 7 6 8 9
'''
################################################################################
class Print_Matrix(object):
    def print_diagonally(self, matrix):

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        M = len(matrix)
        N = len(matrix[0])

        res = []
        count = 0
        row, col = 0, 0
        while count < M * N:
            res.append(matrix[row][col])

            count += 1
            x, y = row, col
            while True:
                x_new = x + 1
                y_new = y - 1

                if x_new < 0 or x_new >= M or y_new < 0 or y_new >= N:
                    break

                res.append(matrix[x_new][y_new])
                count += 1
                x, y = x_new, y_new
            if col == N - 1:
                row += 1
            else:
                col += 1
        return res



a = Print_Matrix()
#print a.print_diagonally([[1, 2], [3, 4]])
print a.print_diagonally([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])

