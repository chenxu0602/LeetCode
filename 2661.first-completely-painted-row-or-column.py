#
# @lc app=leetcode id=2661 lang=python3
#
# [2661] First Completely Painted Row or Column
#

# @lc code=start
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        m, n = map(len, (mat, mat[0]))
        loc = {x: (i, j) for i, row in enumerate(mat) for j, x in enumerate(row)}
        rows, cols = [0] * m, [0] * n
        for k, x in enumerate(arr):
            i, j = loc[x]
            rows[i] += 1
            cols[j] += 1
            if rows[i] == n or cols[j] == m:
                return k
        
# @lc code=end

