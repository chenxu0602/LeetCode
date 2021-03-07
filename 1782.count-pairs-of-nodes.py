#
# @lc app=leetcode id=1782 lang=python3
#
# [1782] Count Pairs Of Nodes
#
# https://leetcode.com/problems/count-pairs-of-nodes/description/
#
# algorithms
# Hard (21.96%)
# Likes:    46
# Dislikes: 37
# Total Accepted:    841
# Total Submissions: 3.8K
# Testcase Example:  '4\n[[1,2],[2,4],[1,3],[2,3],[2,1]]\n[2,3]'
#
# You are given an undirected graph represented by an integer n, which is the
# number of nodes, and edges, where edges[i] = [ui, vi] which indicates that
# there is an undirected edge between ui and vi. You are also given an integer
# array queries.
# 
# The answer to the j^th query is the number of pairs of nodes (a, b) that
# satisfy the following conditions:
# 
# 
# a < b
# cnt is strictly greater than queries[j], where cnt is the number of edges
# incident to a or b.
# 
# 
# Return an array answers such that answers.length == queries.length and
# answers[j] is the answer of the j^th query.
# 
# Note that there can be repeated edges.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
# Output: [6,5]
# Explanation: The number of edges incident to at least one of each pair is
# shown above.
# 
# 
# Example 2:
# 
# 
# Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]],
# queries = [1,2,3,4,5]
# Output: [10,10,9,8,6]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 2 * 10^4
# 1 <= edges.length <= 10^5
# 1 <= ui, vi <= n
# ui != vi
# 1 <= queries.length <= 20
# 0 <= queries[j] < edges.length
# 
# 
#

# @lc code=start
from collections import defaultdict, Counter
import itertools

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:

        # ans = []

        # nodeDegrees = [0] * (n + 1)
        # edgeDegrees = defaultdict(int)

        # for u, v in edges:
        #     edgeDegrees[min(u, v), max(u, v)] += 1
        #     nodeDegrees[u] += 1
        #     nodeDegrees[v] += 1

        # sortedNodeDegrees = sorted(nodeDegrees[1:])

        # for q in queries:
        #     cnt = 0

        #     tail = n
        #     for head in range(0, n - 1):
        #         tail = max(tail, head + 1)
        #         while tail - 1 > head and sortedNodeDegrees[head] + sortedNodeDegrees[tail - 1] > q:
        #             tail -= 1
        #         cnt += n - tail

        #     for u, v in edgeDegrees:
        #         if nodeDegrees[u] + nodeDegrees[v] - edgeDegrees[(u, v)] <= q < nodeDegrees[u] + nodeDegrees[v]:
        #             cnt -= 1

        #     ans.append(cnt)

        # return ans


        nodes = {i: 0 for i in range(1, n + 1)}
        pairs = defaultdict(int)

        for u, v in edges:
            nodes[u] += 1
            nodes[v] += 1
            pairs[(min(u, v), max(u, v))] += 1

        ans = [0] * (2 * max(nodes.values()) + 2)
        counter = Counter(nodes.values())

        for i, j in itertools.product(counter, counter):
            if i < j: ans[i + j] += counter[i] * counter[j]
            if i == j: ans[i + j] += counter[i] * (counter[j] - 1) // 2

        for i, j in pairs:
            ans[nodes[i] + nodes[j]] -= 1
            ans[nodes[i] + nodes[j] - pairs[i, j]] += 1

        for i in range(len(ans) - 2, -1, -1):
            ans[i] += ans[i + 1]

        return [ans[min(query + 1, len(ans) - 1)] for query in queries]
        





        
# @lc code=end

