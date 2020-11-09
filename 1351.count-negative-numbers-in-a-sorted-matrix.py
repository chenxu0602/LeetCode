#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
#
# algorithms
# Easy (76.09%)
# Likes:    610
# Dislikes: 39
# Total Accepted:    75.1K
# Total Submissions: 98.8K
# Testcase Example:  '[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]'
#
# Given a m * n matrix grid which is sorted in non-increasing order both
# row-wise and column-wise. 
# 
# Return the number of negative numbers in grid.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[3,2],[1,0]]
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# 
# 
# Example 4:
# 
# 
# Input: grid = [[-1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
# 
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # O(m + n)
        # m, n = map(len, (grid, grid[0]))
        # r, c, cnt = 0, n - 1, 0
        # while r < m and c >= 0:
        #     if grid[r][c] < 0:
        #         cnt += m - r
        #         c -= 1
        #     else:
        #         r += 1

        # return cnt


        # O(mlogn)
        res = 0
        start = 0 
        m, n = map(len, (grid, grid[0]))

        def binary_search(row, lo, hi):
            while lo < hi:
                mi = (lo + hi) // 2
                if row[mi] < 0:
                    hi = mi
                else:
                    lo = mi + 1
            return lo if row[lo] < 0 else -1

        lo, hi = 0, n - 1
        for i, row in enumerate(grid[::-1]):
            j = binary_search(row, lo, hi)
            if j < 0: break
            res += n - j
            lo = j

        return res
        
# @lc code=end

