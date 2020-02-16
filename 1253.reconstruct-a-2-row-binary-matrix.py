#
# @lc app=leetcode id=1253 lang=python3
#
# [1253] Reconstruct a 2-Row Binary Matrix
#
# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/description/
#
# algorithms
# Medium (38.94%)
# Likes:    75
# Dislikes: 8
# Total Accepted:    7.6K
# Total Submissions: 19.5K
# Testcase Example:  '2\n1\n[1,1,1]'
#
# Given the following details of a matrix with n columns and 2 rows :
# 
# 
# The matrix is a binary matrix, which means each element in the matrix can be
# 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum
# is given as an integer array with length n.
# 
# 
# Your task is to reconstruct the matrix with upper, lower and colsum.
# 
# Return it as a 2-D integer array.
# 
# If there are more than one valid solution, any of them will be accepted.
# 
# If no valid solution exists, return an empty 2-D array.
# 
# 
# Example 1:
# 
# 
# Input: upper = 2, lower = 1, colsum = [1,1,1]
# Output: [[1,1,0],[0,0,1]]
# Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct
# answers.
# 
# 
# Example 2:
# 
# 
# Input: upper = 2, lower = 3, colsum = [2,2,1,1]
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= colsum.length <= 10^5
# 0 <= upper, lower <= colsum.length
# 0 <= colsum[i] <= 2
# 
# 
#

# @lc code=start
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:

        n = len(colsum)
        upper_list, lower_list = [0] * n, [0] * n

        for i, v in enumerate(colsum):
            if v == 1:
                if upper > lower:
                    upper_list[i] = 1
                    upper -= 1
                else:
                    lower_list[i] = 1
                    lower -= 1
            elif v == 2:
                upper_list[i] = lower_list[i] = 1
                upper -= 1; lower -= 1

        return [upper_list, lower_list] if upper == lower == 0 else []
        
# @lc code=end

