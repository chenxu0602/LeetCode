#
# @lc app=leetcode id=2250 lang=python3
#
# [2250] Count Number of Rectangles Containing Each Point
#

# @lc code=start
from collections import defaultdict
import bisect

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:

        res = []
        n = len(rectangles)
        dic = defaultdict(list)
        for l, h in rectangles:
            dic[h].append(l)

        for h in dic:
            dic[h].sort()

        for x, y in points:
            count = 0
            for h in range(y, 101):
                j = bisect.bisect_left(dic[h], x)
                count += len(dic[h]) - j
            res.append(count)

        return res
        
# @lc code=end

