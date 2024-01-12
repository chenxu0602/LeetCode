#
# @lc app=leetcode id=2976 lang=python3
#
# [2976] Minimum Cost to Convert String I
#

# @lc code=start
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        graph = [[float('inf')] * 26  for _ in range(26)]
        n = len(original)

        for i in range(26):
            graph[i][i] = 0

        for i in range(n):
            graph[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')] = min(graph[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')], cost[i])

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


        ans = 0
        for i in range(len(source)):
            ans += graph[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
            if ans >= float('inf'):
                return -1

        return ans

        
        
# @lc code=end

