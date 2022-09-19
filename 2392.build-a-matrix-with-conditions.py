#
# @lc app=leetcode id=2392 lang=python3
#
# [2392] Build a Matrix With Conditions
#

# @lc code=start
from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def helper(A):
            nxt, in_degree = [set() for _ in range(k)], [0] * k
            dq, ans = deque(), []
            A = set([tuple(a) for a in A])

            for i, j in A:
                nxt[i - 1].add(j - 1)
                in_degree[j - 1] += 1

            for i in range(k):
                if in_degree[i] == 0:
                    dq.append(i)

            while dq:
                cur = dq.popleft()
                ans.append(cur)
                for cand in nxt[cur]:
                    in_degree[cand] -= 1
                    if in_degree[cand] == 0:
                        dq.append(cand)

            return ans if len(ans) == k else []

        ans1, ans2 = helper(rowConditions), helper(colConditions)
        if not ans1 or not ans2: return []

        A = [[0] * k for _ in range(k)]
        for i in range(k):
            A[ans1.index(i)][ans2.index(i)] = i + 1
        return A
        
# @lc code=end

