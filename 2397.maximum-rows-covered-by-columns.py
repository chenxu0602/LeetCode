#
# @lc app=leetcode id=2397 lang=python3
#
# [2397] Maximum Rows Covered by Columns
#

# @lc code=start
from itertools import combinations

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = map(len, (matrix, matrix[0]))
        maxRows = 0

        colToChoose = list(combinations(list(range(n)), numSelect))

        for col in colToChoose:
            col = set(col)
            rowHidden = 0
            for row in matrix:
                canHide = True
                for i in range(n):
                    if row[i] and i not in col:
                        canHide = False
                        break

                if canHide:
                    rowHidden += 1

            maxRows = max(maxRows, rowHidden)

        return maxRows
        
# @lc code=end

