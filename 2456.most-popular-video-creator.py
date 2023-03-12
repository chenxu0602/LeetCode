#
# @lc app=leetcode id=2456 lang=python3
#
# [2456] Most Popular Video Creator
#

# @lc code=start
from collections import defaultdict

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        tot, vid = defaultdict(int), defaultdict(list)

        for c, i, v in zip(creators, ids, views):
            tot[c] += v
            vid[c].append((-v, i))

        m = max(tot.values())
        return [[c, min(v)[1]] for c, v in vid.items() if tot[c] == m]
        
# @lc code=end

