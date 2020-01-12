#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (39.30%)
# Likes:    707
# Dislikes: 20
# Total Accepted:    27.9K
# Total Submissions: 70.8K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n matrix of positive integers representing the height of each
# unit cell in a 2D elevation map, compute the volume of water it is able to
# trap after raining.
# 
# 
# 
# Note:
# 
# Both m and n are less than 110. The height of each unit cell is greater than
# 0 and is less than 20,000.
# 
# 
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
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        heap = []
        water = 0

        for r in range(rows):
            heapq.heappush(heap, (heightMap[r][0], r, 0))
            heapq.heappush(heap, (heightMap[r][cols-1], r, cols-1))
        for c in range(cols):
            heapq.heappush(heap, (heightMap[0][c], 0, c))
            heapq.heappush(heap, (heightMap[rows-1][c], rows-1, c))

        visited = {(r, c) for _, r, c in heap}

        while heap:

            h, r, c = heapq.heappop(heap)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r1, c1 = r + dr, c + dc
                if (r1, c1) not in visited and 0 <= r1 < rows and 0 <= c1 < cols:
                    visited.add((r1, c1))
                    water += max(0, h - heightMap[r1][c1])
                    heapq.heappush(heap, (max(h, heightMap[r1][c1]), r1, c1))

        return water


        

