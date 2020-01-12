#
# @lc app=leetcode id=850 lang=python3
#
# [850] Rectangle Area II
#
# https://leetcode.com/problems/rectangle-area-ii/description/
#
# algorithms
# Hard (45.54%)
# Likes:    211
# Dislikes: 23
# Total Accepted:    7.9K
# Total Submissions: 17.3K
# Testcase Example:  '[[0,0,2,2],[1,0,2,3],[1,0,3,1]]'
#
# We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1,
# y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner,
# and (x2, y2) are the coordinates of the top-right corner of the ith
# rectangle.
# 
# Find the total area covered by all rectangles in the plane.  Since the answer
# may be too large, return it modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: As illustrated in the picture.
# 
# 
# Example 2:
# 
# 
# Input: [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 =
# (-7)^2 = 49.
# 
# 
# Note:
# 
# 
# 1 <= rectangles.length <= 200
# rectanges[i].length = 4
# 0 <= rectangles[i][j] <= 10^9
# The total area covered by all rectangles will never exceed 2^63 - 1 and thus
# will fit in a 64-bit signed integer.
# 
#
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:

        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]] + [0]))
        x_i = {v: i for i, v in enumerate(xs)}
        count = [0] * len(x_i)
        L = []

        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])

        L.sort()
        cur_y = cur_x_sum = area = 0

        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig

            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)



