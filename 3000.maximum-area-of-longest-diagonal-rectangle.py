#
# @lc app=leetcode id=3000 lang=python3
#
# [3000] Maximum Area of Longest Diagonal Rectangle
#

# @lc code=start
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        a, b = max(dimensions, key=lambda x: (x[0]*x[0] + x[1]*x[1], x[0] * x[1]))
        return a * b
        
# @lc code=end

