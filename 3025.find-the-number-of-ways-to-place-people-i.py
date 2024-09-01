#
# @lc app=leetcode id=3025 lang=python3
#
# [3025] Find the Number of Ways to Place People I
#

# @lc code=start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: (x[0], -x[1]))
        n, cnt = len(points), 0
        for i in range(n):
            y = float('-inf')
            for j in range(i + 1, n):
                if points[i][1] >= points[j][1] > y:
                    cnt += 1
                    y = points[j][1]

        return cnt
        
        
# @lc code=end

