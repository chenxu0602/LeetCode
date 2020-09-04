#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (45.19%)
# Likes:    1072
# Dislikes: 202
# Total Accepted:    67.8K
# Total Submissions: 150.2K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# There are N network nodes, labelled 1 to N.
# 
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
# 
# Now, we send a signal from a certain node K. How long will it take for all
# nodes to receive the signal? If it is impossible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
# 
# 
#

# @lc code=start
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # Depth-First Search
        # Time  complexity: O(N^N + ElogE) where E is the length of times.
        # Space compleixty: O(N + E), the size of graph O(E), plus the size of implicit call stack in our DFS O(N).
        # graph = defaultdict(list)
        # for u, v, w in times:
        #     graph[u].append((w, v))

        # dist = {node: float("inf") for node in range(1, N + 1)}

        # def dfs(node, elapsed):
        #     if elapsed > dist[node]: return
        #     dist[node] = elapsed
        #     for time, nei in sorted(graph[node]):
        #         dfs(nei, elapsed + time)

        # dfs(K, 0)
        # ans = max(dist.values())
        # return ans if ans < float("inf") else -1


        # Dijkstra's Algorithm 
        # Time  complexity: O(N^2)
        # Space complexity: O(N + E)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float("inf") for node in range(1, N + 1)}
        seen = [False] * (N + 1)
        dist[K] = 0

        while True:
            cand_node, cand_dist = -1, float("inf")
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_node, cand_dist = i, dist[i]

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float("inf") else -1
        

        # Dijkstra's Algorithm with Heap
        # Time  complexity: O(NlogN)
        # Space complexity: O(N + E)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq, dist = [(0, K)], {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d + d2, nei))

        return max(dist.values()) if len(dist) == N else -1
# @lc code=end

