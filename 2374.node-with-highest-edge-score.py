#
# @lc app=leetcode id=2374 lang=python3
#
# [2374] Node With Highest Edge Score
#

# @lc code=start
from collections import defaultdict

class Solution:
    def edgeScore(self, edges: List[int]) -> int:

        score = defaultdict(int)

        for u, v in enumerate(edges):
            score[v] += u

        return max(score, key=lambda x: (score[x], -x))
        
# @lc code=end

