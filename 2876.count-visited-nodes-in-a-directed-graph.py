#
# @lc app=leetcode id=2876 lang=python3
#
# [2876] Count Visited Nodes in a Directed Graph
#

# @lc code=start
from collections import OrderedDict

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:

        n = len(edges)
        res = [0] * n

        for i in range(n):
            seen = OrderedDict()
            j = i
            while j not in seen and res[j] == 0:
                seen[j] = len(seen)
                j = edges[j]

            if j in seen:
                k = len(seen) - seen[j]
                for _ in range(k):
                    res[seen.popitem()[0]] = k

            while seen:
                j = seen.popitem()[0]
                res[j] = res[edges[j]] + 1

        return res
        
# @lc code=end

