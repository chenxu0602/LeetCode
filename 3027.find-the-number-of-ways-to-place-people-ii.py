#
# @lc app=leetcode id=3027 lang=python3
#
# [3027] Find the Number of Ways to Place People II
#

# @lc code=start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        n = len(points)
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0

        for i in range(n):
            y = float('-inf')
            for j in range(i + 1, n):
                if points[i][1] >= points[j][1] > y:
                    res += 1
                    y = points[j][1]

        return res
        
# @lc code=end

