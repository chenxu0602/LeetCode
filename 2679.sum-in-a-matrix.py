#
# @lc app=leetcode id=2679 lang=python3
#
# [2679] Sum in a Matrix
#

# @lc code=start
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        return sum(map(max, zip(*map(sorted, nums))))
        
# @lc code=end

