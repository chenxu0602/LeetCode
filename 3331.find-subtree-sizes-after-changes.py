#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        # n = len(parent)
        # newParent = parent + []
        # newCount = [1] * n

        # for i in range(1, n):
        #     p = parent[i]
        #     while p != -1:
        #         if s[p] != s[i]:
        #             p = parent[p]
        #         else:
        #             newParent[i] = p
        #             break

        # for i in range(1, n):
        #     p = newParent[i]
        #     while p != -1:
        #         newCount[p] += 1
        #         p = newParent[p]

        # return newCount


        n, clds = len(s), defaultdict(set)
        for i in range(n):
            clds[parent[i]].add(i)
        res = [0] * n

        def dfs(i, anc={}):
            prv, anc[s[i]] = anc.get(s[i]), i
            res[i] = cnt = 1
            for c in clds[i]:
                dfs(c, anc)
                res[parent[c]] += res[c]
            anc[s[i]] = prv
            if prv is not None:
                parent[i] = prv

        dfs(0)
        return res


        
# @lc code=end

