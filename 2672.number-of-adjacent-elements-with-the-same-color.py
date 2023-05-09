#
# @lc app=leetcode id=2672 lang=python3
#
# [2672] Number of Adjacent Elements With the Same Color
#

# @lc code=start
from collections import defaultdict

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:

        ans, d, cnt = [], defaultdict(int), 0

        for i, color in queries:
            if d[i]:
                cnt -= (d[i - 1] == d[i]) + (d[i + 1] == d[i])

            d[i] = color

            if d[i]:
                cnt += (d[i - 1] == d[i]) + (d[i + 1] == d[i])

            ans.append(cnt)

        return ans
        
# @lc code=end

