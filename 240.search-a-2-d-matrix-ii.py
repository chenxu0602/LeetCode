#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
       
        m, n = len(matrix), len(matrix[0]) if matrix else 0       

        i, j = 0, n - 1
        while i < m and j >= 0:
            val = matrix[i][j]
            if val == target:
                return True
            elif val < target:
                i += 1
            else:
                j -= 1

        return False

        """
        j = -1
        for row in matrix:
            while j + len(row) and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False
        """
        

