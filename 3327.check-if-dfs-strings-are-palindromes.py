#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:

        t, results = {}, {}

        for i in range(len(parent)):
            p = parent[i]
            t[p] = t.get(p, []) + [i]

        def dfs(x):
            if x not in t:
                results[x] = True
                return s[x]
            st = ""
            for v in t[x]:
                st += dfs(v)
            st += s[x]
            if st[::-1] == st:
                results[x] = True
            return st
            

        dfs(-1)

        ans = [False] * len(parent)
        for i in results.keys():
            ans[i] = results[i]

        return ans

        
# @lc code=end

