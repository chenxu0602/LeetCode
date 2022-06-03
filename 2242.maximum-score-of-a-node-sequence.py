#
# @lc app=leetcode id=2242 lang=python3
#
# [2242] Maximum Score of a Node Sequence
#

# @lc code=start
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        edge = [[] for _ in range(n)]
        for u, v in edges:
            edge[u].append(v)
            edge[v].append(u)

        for l in edge:
            l.sort(key=lambda x: scores[x], reverse=True)

        ans = -1
        for u, v in edges:
            for x1 in range(min(3, len(edge[u]))):
                for y1 in range(min(3, len(edge[v]))):
                    x, y = edge[u][x1], edge[v][y1]
                    if x != u and x != v and y != u and y != v and x != y:
                        ans = max(ans, scores[u] + scores[v] + scores[x] + scores[y])

        return ans
        
# @lc code=end

