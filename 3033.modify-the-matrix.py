#
# @lc app=leetcode id=3033 lang=python3
#
# [3033] Modify the Matrix
#

# @lc code=start
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        t = [*zip(*matrix)]
        return [[(v, max(t[i]))[v < 0] for i, v in enumerate(row)] for row in matrix]
        
# @lc code=end

