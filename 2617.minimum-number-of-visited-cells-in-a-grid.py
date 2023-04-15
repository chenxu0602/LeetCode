#
# @lc app=leetcode id=2617 lang=python3
#
# [2617] Minimum Number of Visited Cells in a Grid
#

# @lc code=start
from collections import deque
import heapq

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:

        # For every row and column store a minHeap with values being a tuple of (score, maxReachablRow/Col) . And always pick the smallest score from both minHeaps.
        # Then for every cell we'll just pick the smallest score from row or column that can be obtained based on previous cells in row/col.

        # Time  complexity: O(mn(mlogm + nlogn))
        # Space complexity: O(mn)

        m, n = map(len, (grid, grid[0]))
        bestRow = [[] for _ in range(m)] # will store (minScore, maxReachableColumn) for each row
        bestCol = [[] for _ in range(n)] # will store (minScore, maxReachableRow) for each column

        heapq.heappush(bestRow[0], (1, 0))
        for i in range(m):
            for j in range(n):
                minScore = float("inf")

                # removing scores that are not reaching this cell
                while bestRow[i] and bestRow[i][0][1] < j:
                    heapq.heappop(bestRow[i])

                if bestRow[i]:
                    minScore = min(minScore, bestRow[i][0][0])

                while bestCol[j] and bestCol[j][0][1] < i:
                    heapq.heappop(bestCol[j])

                if bestCol[j]:
                    minScore = min(minScore, bestCol[j][0][0])

                if (i, j) == (m - 1, n - 1) and minScore != float("inf"):
                    return minScore

                if minScore != float("inf"):
                    heapq.heappush(bestRow[i], (minScore + 1, j + grid[i][j]))
                    heapq.heappush(bestCol[j], (minScore + 1, i + grid[i][j]))

        return -1

        
# @lc code=end

