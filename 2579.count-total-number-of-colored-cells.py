#
# @lc app=leetcode id=2579 lang=python3
#
# [2579] Count Total Number of Colored Cells
#

# @lc code=start
class Solution:
    def coloredCells(self, n: int) -> int:

        # return n * n + (n - 1) * (n - 1)

        return 2 * n * (n - 1) + 1
        
# @lc code=end

