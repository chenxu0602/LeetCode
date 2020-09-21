#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#
# https://leetcode.com/problems/minimum-area-rectangle/description/
#
# algorithms
# Medium (52.00%)
# Likes:    494
# Dislikes: 97
# Total Accepted:    37.7K
# Total Submissions: 72.3K
# Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
#
# Given a set of points in the xy-plane, determine the minimum area of a
# rectangle formed from these points, with sides parallel to the x and y axes.
# 
# If there isn't any rectangle, return 0.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
# 
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Sort by Column
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx, ans = {}, float("inf")

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x

        return ans if ans < float("inf") else 0


        # Count by Diagonal
        # For each pair of points in the array, consider them to be the long diagonal of a potential rectangle. We can check if all 4 points are there using a Set.
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        # S = set(map(tuple, points))
        # ans = float("inf")
        # for j, p2 in enumerate(points):
        #     for i in range(j):
        #         p1 = points[i]
        #         if p1[0] != p2[0] and p1[1] != p2[1] and \
        #             (p1[0], p2[1]) in S and (p2[0], p1[1]) in S:
        #             ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        # return ans if ans < float("inf") else 0
        
# @lc code=end

