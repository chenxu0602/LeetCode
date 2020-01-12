#
# @lc app=leetcode id=296 lang=python3
#
# [296] Best Meeting Point
#
# https://leetcode.com/problems/best-meeting-point/description/
#
# algorithms
# Hard (54.88%)
# Likes:    270
# Dislikes: 21
# Total Accepted:    24.8K
# Total Submissions: 45.3K
# Testcase Example:  '[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# A group of two or more people wants to meet and minimize the total travel
# distance. You are given a 2D grid of values 0 or 1, where each 1 marks the
# home of someone in the group. The distance is calculated using Manhattan
# Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
# 
# Example:
# 
# 
# Input: 
# 
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 
# Output: 6 
# 
# Explanation: Given three people living at (0,0), (0,4), and
# (2,2):
# The point (0,2) is an ideal meeting point, as the total travel
# distance 
# of 2+2+2=6 is minimal. So return 6.
# 
#
class Solution:
    def minDistance1D(self, points):
        dist = 0
        i, j = 0, len(points) - 1

        while i < j:
            dist += points[j] - points[i]
            i += 1
            j -= 1

        return dist

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [i for i in range(m) for j in range(n) if grid[i][j] == 1]
        cols = [j for j in range(n) for i in range(m) if grid[i][j] == 1]

        return self.minDistance1D(rows) + self.minDistance1D(cols)
        

