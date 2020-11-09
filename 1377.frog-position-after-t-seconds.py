#
# @lc app=leetcode id=1377 lang=python3
#
# [1377] Frog Position After T Seconds
#
# https://leetcode.com/problems/frog-position-after-t-seconds/description/
#
# algorithms
# Hard (34.09%)
# Likes:    150
# Dislikes: 56
# Total Accepted:    9.8K
# Total Submissions: 28.7K
# Testcase Example:  '7\n[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]\n2\n4'
#
# Given an undirected tree consisting of n vertices numbered from 1 to n. A
# frog starts jumping from the vertex 1. In one second, the frog jumps from its
# current vertex to another unvisited vertex if they are directly connected.
# The frog can not jump back to a visited vertex. In case the frog can jump to
# several vertices it jumps randomly to one of them with the same probability,
# otherwise, when the frog can not jump to any unvisited vertex it jumps
# forever on the same vertex. 
# 
# The edges of the undirected tree are given in the array edges, where edges[i]
# = [fromi, toi] means that exists an edge connecting directly the vertices
# fromi and toi.
# 
# Return the probability that after t seconds the frog is on the vertex
# target.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target =
# 4
# Output: 0.16666666666666666 
# Explanation: The figure above shows the given graph. The frog starts at
# vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and
# then jumping with 1/2 probability to vertex 4 after second 2. Thus the
# probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 =
# 1/6 = 0.16666666666666666. 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target =
# 7
# Output: 0.3333333333333333
# Explanation: The figure above shows the given graph. The frog starts at
# vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7
# after second 1. 
# 
# 
# Example 3:
# 
# 
# Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target =
# 6
# Output: 0.16666666666666666
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 100
# edges.length == n-1
# edges[i].length == 2
# 1 <= edges[i][0], edges[i][1] <= n
# 1 <= t <= 50
# 1 <= target <= n
# Answers within 10^-5 of the actual value will be accepted as correct.
# 
# 
#

# @lc code=start
from collections import deque, defaultdict

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        probs = defaultdict(lambda: defaultdict(int))
        probs[1][0] = 1.0

        for T in range(1, t + 1):
            probs2 = probs.copy()
            for u in probs2:
                unvisited = set()
                for v in graph[u]:
                    if v not in probs:
                        unvisited.add(v)

                if len(unvisited) == 0:
                    probs[u][T] = probs[u][T - 1]
                else:
                    for v in unvisited:
                        probs[v][T] = probs[u][T - 1] / len(unvisited)

        return probs[target][t]
        
# @lc code=end

