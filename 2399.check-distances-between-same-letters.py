#
# @lc app=leetcode id=2399 lang=python3
#
# [2399] Check Distances Between Same Letters
#

# @lc code=start
from collections import defaultdict

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = defaultdict(list)

        for i, c in enumerate(s):
            d[c].append(i)

        return all(b - a - 1 == distance[ord(c) - 97] for c, (a, b) in d.items())
        
# @lc code=end

