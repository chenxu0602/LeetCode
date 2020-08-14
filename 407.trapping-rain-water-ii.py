#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (42.26%)
# Likes:    1340
# Dislikes: 31
# Total Accepted:    42.5K
# Total Submissions: 100.1K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n matrix of positive integers representing the height of each
# unit cell in a 2D elevation map, compute the volume of water it is able to
# trap after raining.
# 
# Example:
# 
# 
# Given the following 3x6 height map:
# [
# ⁠ [1,4,3,1,3,2],
# ⁠ [3,2,1,3,2,4],
# ⁠ [2,3,3,2,3,1]
# ]
# 
# Return 4.
# 
# 
# 
# 
# The above image represents the elevation map
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
# 
# 
# 
# 
# 
# After the rain, water is trapped between the blocks. The total volume of
# water trapped is 4.
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 110
# 0 <= heightMap[i][j] <= 20000
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # O(mnlogmn)
        if not heightMap: return 0

        m, n = map(len, (heightMap, heightMap[0]))
        heap, water = [], 0

        for r in range(m):
            heapq.heappush(heap, (heightMap[r][0], r, 0))
            heapq.heappush(heap, (heightMap[r][n - 1], r, n - 1))

        for c in range(n):
            heapq.heappush(heap, (heightMap[0][c], 0, c))
            heapq.heappush(heap, (heightMap[m - 1][c], m - 1, c))

        visited = {(r, c) for _, r, c in heap}

        while heap:
            h, r, c = heappop(heap)
            for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                r1, c1 = r + dr, c + dc
                if (r1, c1) not in visited and 0 <= r1 < m and 0 <= c1 < n:
                    visited.add((r1, c1))
                    water += max(0, h - heightMap[r1][c1])
                    heapq.heappush(heap, (max(h, heightMap[r1][c1]), r1, c1))

        return water
        
# @lc code=end

