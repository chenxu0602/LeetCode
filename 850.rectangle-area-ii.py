#
# @lc app=leetcode id=850 lang=python3
#
# [850] Rectangle Area II
#
# https://leetcode.com/problems/rectangle-area-ii/description/
#
# algorithms
# Hard (47.41%)
# Likes:    368
# Dislikes: 30
# Total Accepted:    13.1K
# Total Submissions: 27.4K
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

# @lc code=start
import itertools
from functools import reduce

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # Principle of Inclusion-Exclusion
        # Time  complexity: O(N x 2^N)
        # Space complexity: O(N)
        # def intersect(rec1, rec2):
        #     return [max(rec1[0], rec2[0]),
        #             max(rec1[1], rec2[1]),
        #             min(rec1[2], rec2[2]),
        #             min(rec1[3], rec2[3])]

        # def area(rec):
        #     dx = max(0, rec[2] - rec[0])
        #     dy = max(0, rec[3] - rec[1])
        #     return dx * dy

        # ans = 0
        # for size in range(1, len(rectangles) + 1):
        #     for group in itertools.combinations(rectangles, size):
        #         ans += (-1) ** (size + 1) * area(reduce(intersect, group))

        # return ans % (10**9 + 7)


        # Coordinate Compression
        # Time  complexity: O(N^3)
        # Space complexity: O(N^2)
        # N = len(rectangles)
        # Xvals, Yvals = set(), set()
        # for x1, y1, x2, y2 in rectangles:
        #     Xvals.add(x1); Xvals.add(x2)
        #     Yvals.add(y1); Yvals.add(y2)

        # imapx = sorted(Xvals)
        # imapy = sorted(Yvals)
        # mapx = {x: i for i, x in enumerate(imapx)}
        # mapy = {y: i for i, y in enumerate(imapy)}

        # grid = [[0] * len(imapy) for _ in imapx]
        # for x1, y1, x2, y2 in rectangles:
        #     for x in range(mapx[x1], mapx[x2]):
        #         for y in range(mapy[y1], mapy[y2]):
        #             grid[x][y] = 1


        # ans = 0
        # for x, row in enumerate(grid):
        #     for y, val in enumerate(row):
        #         if val:
        #             ans += (imapx[x + 1] - imapx[x]) * (imapy[y + 1] - imapy[y])

        # return ans % (10**9 + 7)


        # Line Sweep
        # Time  compleixty: O(N^2 x logN)
        # Space compleixty: O(N)
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        def query():
            ans = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur, x1)
                ans += max(0, x2 - cur)
                cur = max(cur, x2)
            return ans

        active = []
        cur_y = events[0][0]
        ans = 0
        for y, typ, x1, x2 in events:
            ans += query() * (y - cur_y)

            if typ is OPEN:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))

            cur_y = y

        return ans % (10**9 + 7)


        # xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]] + [0]))
        # x_i = {v: i for i, v in enumerate(xs)}
        # count = [0] * len(x_i)
        # L = []

        # for x1, y1, x2, y2 in rectangles:
        #     L.append([y1, x1, x2, 1])
        #     L.append([y2, x1, x2, -1])

        # L.sort() 
        # cur_y = cur_x_sum = area = 0

        # for y, x1, x2, sig in L:
        #     area += (y - cur_y) * cur_x_sum
        #     cur_y = y
        #     for i in range(x_i[x1], x_i[x2]):
        #         count[i] += sig

        #     cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))

        # return area % (10**9 + 7)
# @lc code=end

