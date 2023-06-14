#
# @lc app=leetcode id=2732 lang=python3
#
# [2732] Find a Good Subset of the Matrix
#

# @lc code=start
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:

        m, n = map(len, (grid, grid[0]))
        hsh = {}

        for i in range(m):
            val = 0 # Integer value for the current row

            for j in range(n):
                if grid[i][j] == 1:
                    val += (1 << j)

            if val == 0: return [i]

            for j in range(1, 32):
                if (val & j) == 0 and j in hsh:
                    return [hsh[j], i]

            hsh[val] = i

        return []
        
# @lc code=end

