#
# @lc app=leetcode id=1878 lang=python3
#
# [1878] Get Biggest Three Rhombus Sums in a Grid
#
# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/description/
#
# algorithms
# Medium (43.22%)
# Likes:    89
# Dislikes: 192
# Total Accepted:    4.8K
# Total Submissions: 11.1K
# Testcase Example:  '[[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]'
#
# You are given an m x n integer matrix grid​​​.
# 
# A rhombus sum is the sum of the elements that form the border of a regular
# rhombus shape in grid​​​. The rhombus must have the shape of a square rotated
# 45 degrees with each of the corners centered in a grid cell. Below is an
# image of four valid rhombus shapes with the corresponding colored cells that
# should be included in each rhombus sum:
# 
# Note that the rhombus can have an area of 0, which is depicted by the purple
# rhombus in the bottom right corner.
# 
# Return the biggest three distinct rhombus sums in the grid in descending
# order. If there are less than three distinct values, return all of them.
# 
# 
# Example 1:
# 
# 
# Input: grid =
# [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
# Output: [228,216,211]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums
# are depicted above.
# - Blue: 20 + 3 + 200 + 5 = 228
# - Red: 200 + 2 + 10 + 4 = 216
# - Green: 5 + 200 + 4 + 2 = 211
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [20,9,8]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums
# are depicted above.
# - Blue: 4 + 2 + 6 + 8 = 20
# - Red: 9 (area 0 rhombus in the bottom right corner)
# - Green: 8 (area 0 rhombus in the bottom middle)
# 
# 
# Example 3:
# 
# 
# Input: grid = [[7,7,7]]
# Output: [7]
# Explanation: All three possible rhombus sums are the same, so return [7].
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 10^5
# 
# 
#

# @lc code=start
import heapq, itertools
from functools import lru_cache

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = map(len, (grid, grid[0]))
        heap = []

        def update(heap, num):
            if num not in heap:
                heapq.heappush(heap, num)
                if len(heap) > 3:
                    heapq.heappop(heap)
            return heap

        for num in itertools.chain(*grid):
            update(heap, num)


        @lru_cache(None)
        def dp(i, j, dr):
            if not (0 <= i < m and 0 <= j < n):
                return 0

            return dp(i - 1, j + dr, dr) + grid[i][j]


        for q in range(1, (1 +  min(m, n)) // 2):
            for i in range(q, m - q):
                for j in range(q, n - q):
                    p1 = dp(i + q, j, -1) - dp(i, j - q, -1)
                    p2 = dp(i - 1, j + q - 1, -1) - dp(i - q - 1, j - 1, -1)
                    p3 = dp(i, j - q, 1) - dp(i - q, j, 1)
                    p4 = dp(i + q - 1, j + 1, 1) - dp(i - 1, j + q + 1, 1)
                    update(heap, p1 + p2 + p3 + p4)

        return sorted(heap)[::-1]


        
# @lc code=end

