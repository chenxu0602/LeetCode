#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#

# @lc code=start
from collections import deque
import bisect

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        """
        n = len(parent)
        child_num = [0] * n

        for x in parent[1:]:
            child_num[x] += 1

        longest = [[0] for _ in range(n)]
        queue = deque([(i, 1) for i, v in enumerate(child_num) if v == 0])

        ans = 1
        while queue:
            cur_i, cur_l = queue.popleft()
            cur_p = parent[cur_i]
            child_num[cur_p] -= 1

            if s[cur_p] != s[cur_i]:
                bisect.insort_right(longest[cur_p], cur_l)
                if len(longest[cur_p]) > 2:
                    longest[cur_p].pop(0)

            if child_num[cur_p] == 0:
                ans = max(ans, 1 + sum(longest[cur_p][-2:]))
                queue.append((cur_p, 1 + longest[cur_p][-1]))

        return ans
        """

        children = [[] for _ in range(len(s))]
        for i, j in enumerate(parent):
            if j >= 0:
                children[j].append(i)

        res = [0]
        def dfs(i):
            candidate = [0]
            for j in children[i]:
                cur = dfs(j)
                if s[i] != s[j]:
                    candidate.append(cur)

            candidate = nlargest(2, candidate)
            res[0] = max(res[0], sum(candidate) + 1)
            return max(candidate) + 1

        dfs(0)
        return res[0]


        
# @lc code=end

