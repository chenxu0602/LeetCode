#
# @lc app=leetcode id=2133 lang=python3
#
# [2133] Check if Every Row and Column Contains All Numbers
#

# @lc code=start
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        return all(len(set(row)) == len(matrix) for row in matrix) and all(len(set(col)) == len(matrix) for col in zip(*matrix))
        
# @lc code=end

